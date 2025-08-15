open Printf

let dir = "opere"

let is_png filename =
  let lower = String.lowercase_ascii filename in
  Filename.check_suffix lower ".png"

let () =
  if not (Sys.is_directory dir) then begin
    eprintf "Error: %s is not a directory.\n" dir;
    exit 1
  end;

  let entries = Sys.readdir dir |> Array.to_list in
  let png_files =
    List.filter (fun file ->
      let path = Filename.concat dir file in
      Sys.file_exists path && not (Sys.is_directory path) && is_png file
    ) entries
    |> List.sort String.compare
  in

  let oc = open_out "index.html" in
  fprintf oc {|
<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="icon" href="siteres/icon/favicon.svg" type="image/svg+xml" />
<title>La mia galleria</title>
<style>
@font-face {
  font-family: 'Bebas Neue';
  src: url('siteres/font/BebasNeue-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

body {
  margin: 0;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: lightgray;
  font-family: 'Bebas Neue';
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
|};

  List.iter (fun file ->
    let alt_text =
      try Filename.chop_extension file with _ -> file
    in
    fprintf oc "<img src=\"opere/%s\" loading=\"lazy\" alt=\"%s\" />\n<p>%s</p>\n"
      file alt_text alt_text
  ) png_files;

  fprintf oc "</body>\n</html>\n";
  close_out oc;

  printf "index.html generated successfully with %d images.\n" (List.length png_files)

