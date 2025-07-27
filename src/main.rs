use std::fs::{self, File};
use std::io::{self, Read, Write};
use std::path::Path;

fn main() -> io::Result<()> {
    let image_dir = "opere";

    let mut images: Vec<String> = fs::read_dir(image_dir)?
        .filter_map(|entry| entry.ok())
        .filter_map(|entry| {
            let path = entry.path();
            if path.is_file() {
                path.file_name().and_then(|s| s.to_str()).map(String::from)
            } else {
                None
            }
        })
        .collect();

    images.sort_by(|a, b| a.to_lowercase().cmp(&b.to_lowercase()));

    let mut fhtml = File::create("index.html")?;

    writeln!(fhtml, r#"
<!doctype html>
<html lang="it">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="icon" href="siteres/icon/favicon.svg" type="image/svg+xml" />
<title>La mia galleria</title>
"#)?;

    match File::open("style.css") {
        Ok(mut fcss) => {
            let mut css = String::new();
            fcss.read_to_string(&mut css)?;
            writeln!(fhtml, "<style>\n{}</style>", css)?;
        }
        Err(_) => {
            eprintln!("error open css");
            return Ok(());
        }
    }

    writeln!(fhtml, r#"</head>
<body>"#)?;

    // Write image entries
    for filename in &images {
        let label = Path::new(filename)
            .file_stem()
            .and_then(|s| s.to_str())
            .unwrap_or("unknown");

        writeln!(fhtml, r#"<img src="opere/{}" loading="lazy" alt="{}" />
<p>{}</p>"#, filename, label, label)?;
    }

    writeln!(fhtml, r#"</body>
</html>"#)?;

    println!("DONE");
    Ok(())
}

