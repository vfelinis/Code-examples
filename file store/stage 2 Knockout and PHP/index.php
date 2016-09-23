<?php include 'core/header.php'; ?>

<div class="container">
	<?php
		if(isset($_SESSION['logged_user'])){
			include 'core/spaAuthorized.php';
		}
		else{
			include 'core/notauthorized.php';
		}
	?>
</div>

<?php include 'core/footer.php'; ?>