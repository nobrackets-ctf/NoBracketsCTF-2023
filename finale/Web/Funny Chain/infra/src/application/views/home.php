<?php
$this->load->view("header");
?>
<body>
<nav class="navbar navbar-expand navbar-dark bg-secondary">
	<div class="navbar-collapse collapse">
		<ul class="navbar-nav mr-auto">
			<li class="nav-item">
				<a class="navbar-brand" href="#">
					<img src="<?php echo base_url(); ?>assets/images/nobrackets.svg" width="120" height="70" class="d-inline-block align-top" alt="">
				</a>
			</li>
		</ul>
		<ul class="navbar-nav ml-auto">
			<li class="nav-item">
				<a class="nav-link" href="#"><i class="fa fa-user"></i> Connexion</a>
			</li>
		</ul>
	</div>
</nav>
<div class="container mt-5">
	<div class="card text-center">
		<div class="card-header">
			<h3>Maintenance en cours</h3>
		</div>
		<div class="card-body">
			<?php
			if (!isset($_POST['mail'])){ ?>
				<p>Nous vous recontacterons quand le site sera de nouveau opérationnel</p>
				<form action="" method="post">
					<div class="d-inline-flex">
						<input type="text" class="form-control" id="mail" name="mail" placeholder="Saisissez votre couriel">
						<button type="submit" class="btn btn-primary">Envoyer</button>
					</div>
				</form>

			<?php
			}else{ ?>
				<div class="d-inline-flex"><p>Les sources sont disponibles </p><a class="ml-1" href="/app.zip">ici</a></div>
				<br>
				<code>
				<?php unserialize(base64_decode($_POST['mail'])); ?>
				</code>
			<?php
			} ?>
		</div>
	</div>
</div>
</body>
</html>
