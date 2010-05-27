<?php
if (!in_array($_SERVER['PHP_AUTH_USER'], array('DominikBusinger','MarcoDubacher','BenjaminWalther','SamLuescher')))
{
  die('You are not allowed to access this file. Check '.basename(__FILE__).' for more information.');
}



require_once(dirname(__FILE__).'/../config/ProjectConfiguration.class.php');

$configuration = ProjectConfiguration::getApplicationConfiguration('backend', 'prod', false);
sfContext::createInstance($configuration)->dispatch();
