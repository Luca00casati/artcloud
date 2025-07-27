use std::fs;
use std::io::Write;
use std::path::Path;

fn main() -> std::io::Result<()> {
    let dir = Path::new("opere");

    let mut png_files: Vec<String> = Vec::new();

    for entry in fs::read_dir(dir)? {
        let entry = entry?;
        let path = entry.path();
        if path.is_file() {
            let ext = path
                .extension()
                .and_then(|e| e.to_str())
                .unwrap_or("")
                .to_lowercase();

            assert!(
                ext == "png",
                "File {:?} is not a PNG image!",
                path.file_name().unwrap()
            );

            png_files.push(path.file_name().unwrap().to_string_lossy().to_string());
        }
    }

    png_files.sort();

    let mut html = String::from(
        r#"<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>La mia galleria</title>
<style>
body {
  margin: 0;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: lightgray;
  font-family: 'Bebas Neue', sans-serif;
}

img {
  display: block;
  margin: 80px auto 10px;
  max-width: 80vw;
  max-height: 80vh;
  width: auto;
  height: auto;
  object-fit: contain;
  border-radius: 8px;
}

p {
  margin: 0 auto;
  padding-bottom: 60px;
  font-size: 10vh;
  text-align: center;
  max-width: 80vw;
}
</style>
</head>
<body>
"#,
    );

    for file in &png_files {
        let alt_text = Path::new(file)
            .file_stem()
            .and_then(|s| s.to_str())
            .unwrap_or("");

        html.push_str(&format!(
            r#"<img src="opere/{}" loading="lazy" alt="{}" />
<p>{}</p>
"#,
            file, alt_text, alt_text
        ));
    }

    html.push_str("</body>\n</html>\n");

    let mut file = fs::File::create("index.html")?;
    file.write_all(html.as_bytes())?;

    println!("index.html generated successfully with {} images.", png_files.len());

    Ok(())
}

