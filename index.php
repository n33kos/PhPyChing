<html>
	<head>
		<link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono' rel='stylesheet' type='text/css'>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
		<link href='style.css' rel='stylesheet' type='text/css'>
	</head>
	<body>
		<div class="container margin-bottom-15">
			<?php
				$isSubmitted = false;
				if(isset($_GET["string"])){
					$theString = $_GET["string"];
				}
				if(isset($theString)){
					$isSubmitted = true;
				}

				if($isSubmitted == true){
					//GET string var from url
					$getURLarg = " " . $_GET["string"];
					//escape statement for shell
					$command = escapeshellcmd('python PhPyChing.py' . (string)$getURLarg);
					//execute command plus string var as argument
					$output = shell_exec($command);
					//Print the results from python
					echo $output;
					echo '<br><a href="/iching/"> < Back</a>';
				}else{
					echo '<h1 class="text-center">Enter Your Question:</h1><div class="row"><div class="col-sm-6 col-sm-offset-3"><form action="" class="text-center"><input class="form-control" name="string"></div><div class="col-sm-4 col-sm-offset-4"><button class="btn btn-primary btn-block" type="submit">Cast</button></form></div>';	
				}
			?>
		</div>
		<div class="colorcube Earth">&nbsp;</div>
		<div class="colorcube Mountain">&nbsp;</div>
		<div class="colorcube Water">&nbsp;</div>
		<div class="colorcube Wood">&nbsp;</div>
		<div class="colorcube Thunder">&nbsp;</div>
		<div class="colorcube Fire">&nbsp;</div>
		<div class="colorcube Lake">&nbsp;</div>
		<div class="colorcube Heaven">&nbsp;</div>
	</body>
</html>
