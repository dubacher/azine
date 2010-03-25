<?php

/**
 * sfGuardUser form.
 *
 * @package    azine
 * @subpackage form
 * @author     DominikBusinger
 * @version    SVN: $Id: sfDoctrinePluginFormTemplate.php 23810 2009-11-12 11:07:44Z Kris.Wallsmith $
 */
class sfGuardUserForm extends PluginsfGuardUserForm
{
  public function configure()
  {
  	// hide some of the fields
  	$this->setWidget('username', new sfWidgetFormInputHidden());
  	$this->setWidget('algorithm', new sfWidgetFormInputHidden());
  	$this->setWidget('salt', new sfWidgetFormInputHidden());
  	$this->setWidget('is_active', new sfWidgetFormInputHidden());
  	$this->setWidget('is_super_admin', new sfWidgetFormInputHidden());
  	$this->setWidget('last_login', new sfWidgetFormInputHidden());
  	$this->setWidget('created_at', new sfWidgetFormInputHidden());
  	$this->setWidget('updated_at', new sfWidgetFormInputHidden());
  	$this->setWidget('slug', new sfWidgetFormInputHidden());
  	$this->setWidget('groups_list', new sfWidgetFormInputHidden());
  	$this->setWidget('permissions_list', new sfWidgetFormInputHidden());

  	// redefine the others.
  	$this->setWidget('notification_mode', new sfWidgetFormChoice(array('choices'=>sfConfig::get('app_user_notification_modes'))));
  	$this->setWidget('cv_url', new sfWidgetFormInputText());
  	
  	// define the validators
  	$this->setValidator('email_address', new sfValidatorEmail());
  }
	}
