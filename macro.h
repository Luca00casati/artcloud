#define MACRO0 \
<!doctype html> \
<html lang="it"> \
<head> \
  <meta charset="UTF-8" /> \
  <meta name="viewport" content="width=device-width, initial-scale=1.0" /> \
  <link rel="icon" href="siteres/icon/favicon.svg" type="image/svg+xml" /> \
  <title>La mia galleria</title> 

#define MACRO1 \
</head> \
<body>

#define MACRO2 \
</body> \
</html>

#define DIR operejwebp
#define IMAGETYPE webp
#define IMAGE(X) <img src=DIR/X.IMAGETYPE loading=lazy alt=X  /><p>X</p>

//site
MACRO0
#include "style.css"
MACRO1
IMAGE(firepunch)
IMAGE(faccia)
IMAGE(rosa)
IMAGE(Puccini)
IMAGE(tauros)
IMAGE(frieren)
MACRO2
