<!DOCTYPE html>
<html lang="en">
<head>
  <title>Speech Recognition</title>
  <link rel="stylesheet" href="test.css">
</head>
<body>
    
 <div id=div class="shadowbox" style="top:100px ">
     <h1 style="text-align: center">Drawing Shape</h1>
  <div class="container"> <!--page container -->
    <div class="text-box" contenteditable="true"></div>
    <i class="fa fa-microphone"></i> 
       
  </div>
     <button type="submit" class="btn" onclick="doSomething();">Submit</a>
     <form action="" method="POST" enctype="multipart/form-data">
     <button class="btn" name = "home" style=" padding: 10px 40px">Back To Home</button>
         </form>
    </div>
  <audio class="sound" src="chime.mp3"></audio> <!-- sound to be played when we click icon -->
   
  <script src="index.js"></script>
</body>
    <?php

        if (isset($_POST['home']))
        {
            header('Location:/gui/web.html');
        }
?>
</html>