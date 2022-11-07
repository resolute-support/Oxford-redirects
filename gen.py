import string
import random

letters = string.ascii_lowercase

for i in range(20):
    filename = ''.join(random.choice(letters) for i in range(10))
    filename = filename+".html"
    f = open(filename, "w")
    f.write("""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <script type="text/javascript">
      window.location.replace("https://resolute.education");
    </script>
  </body>
</html>
    """)
    f.close()
    print("created files")
