<html>
	<head>
		<link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono' rel='stylesheet' type='text/css'>
		<link href='style.css' rel='stylesheet' type='text/css'>
	</head>
	<body>
		<p>&nbsp;</p>
		<div class="container">
			<?php
				$isSubmitted = false;
				$theString = $_GET["string"];
				if($theString)
					$isSubmitted = true;

				if($isSubmitted){
					//GET string var from url
					$getURLarg = " " . $_GET["string"];
					//escape statement for shell
					$command = escapeshellcmd('python PhPyChing.py' . (string)$getURLarg);
					//execute command plus string var as argument
					$output = shell_exec($command);
					//Print the results from python
					echo $output;
					echo '<br><br><br><br><a href="/iching/"> < Back</a>';
				}else{
					echo '<h1 class="text-center">Enter Your Question:</h1><form action="" class="text-center"><input name="string"><br><br><button type="submit">Cast</button></form>';	
				}
			?>
		</div>
		<p>&nbsp;</p>
	</body>
</html>
