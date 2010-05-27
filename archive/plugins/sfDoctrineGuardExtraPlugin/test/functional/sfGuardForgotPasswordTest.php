<?php

include(dirname(__FILE__).'/../bootstrap/functional.php');

$user_data = array(
  'username'      => 'sfGuardPasswordTest'.time(),
  'password'      => 'sfGuardPasswordTest',
  'email_address' => 'sfGuardPasswordTest'.time().'@domain.de',
);

$sf_guard_user = new sfGuardUser();
$sf_guard_user->fromArray($user_data);
$sf_guard_user->save();

$form     = new sfGuardFormForgotPassword();
$formName = $form->getName();

$browser = new sfTestFunctional(new sfBrowser());

$browser->
  info('1. show request')->
  get('/request_password')->

  with('request')->begin()->
    isParameter('module', 'sfGuardForgotPassword')->
    isParameter('action', 'password')->
  end()->

  with('response')->begin()->
    isValid(true)->
    isStatusCode(200)->
    checkForm($form)->
  end()->

  click('request')->

  with('request')->begin()->
    isParameter('module', 'sfGuardForgotPassword')->
    isParameter('action', 'password')->
  end()->

  with('form')->begin()->
    hasErrors(1)->
    isError('username_or_email_address', 'required')->
  end()->

  with('response')->begin()->
    isRedirected(false)->
    isStatusCode(200)->
    isValid(true)->
  end()->

  setField($formName.'[username_or_email_address]', 'alpha')->
  click('request')->

  with('form')->begin()->
    hasErrors(1)->
    isError('username_or_email_address', 'invalid')->
  end()->

  setField($formName.'[username_or_email_address]', $user_data['email_address'])->
  click('request')->

  info('2. action')->
  with('request')->begin()->
    isParameter('module', 'sfGuardForgotPassword')->
    isParameter('action', 'password')->
  end()->

  with('form')->begin()->
    hasErrors(false)->
  end()->

  with('mailer')->begin()->
    hasSent(1)->
    checkHeader('From', sfConfig::get('app_sf_guard_extra_plugin_from'))->
    checkHeader('Subject', 'Request to reset password')->
  end()->

  with('response')->begin()->
    isRedirected(true)->
    followRedirect()->
  end()->

  info('3. success page')->
  with('request')->begin()->
    isParameter('module', 'sfGuardForgotPassword')->
    isParameter('action', 'request_reset_password')->
  end()->

  with('response')->begin()->
    isStatusCode(200)->
    isValid(true)->
  end()
;

$passwordOld = $sf_guard_user['password'];
$passwordNew = time();

$browser->
  info('4. show reset')->
  get('/reset_password/'.$passwordOld.'/'.$sf_guard_user['id'])->

  with('request')->begin()->
    isParameter('module', 'sfGuardForgotPassword')->
    isParameter('action', 'reset_password')->
    isParameter('id', $sf_guard_user['id'])->
    isParameter('key', $passwordOld)->
  end()->

  with('mailer')->begin()->
    hasSent(1)->
    checkHeader('From', sfConfig::get('app_sf_guard_extra_plugin_from'))->
    checkHeader('Subject', 'Password reset successfully')->
  end()->

  with('response')->begin()->
    isStatusCode(200)->
    isValid(true)->
  end()->

  info('5. invalid key')->
  get('/reset_password/invalidKey/'.$sf_guard_user['id'])->
  with('request')->begin()->
    isParameter('module', 'sfGuardForgotPassword')->
    isParameter('action', 'reset_password')->
  end()->
  isForwardedTo('sfGuardForgotPassword', 'invalid_key')->

  info('6. check new login')->
  get('/login')->
  setField('signin[username]', $user_data['username'])->
  setField('signin[password]', $passwordNew)->
  click('sign in')->

  with('user')->begin()->
    isAuthenticated(true)->
  end()->

  info('7. redirect when authenticated')->
  get('/request_password')->
  with('response')->begin()->
    isRedirected(true)->
  end()
;

$sf_guard_user->delete();

$browser->
  restart()->

  info('8. deleted user')->
  get('/request_password')->
  setField($formName.'[username_or_email_address]', $user_data['email_address'])->
  click('request')->

  with('form')->begin()->
    hasErrors(1)->
  end()
;
