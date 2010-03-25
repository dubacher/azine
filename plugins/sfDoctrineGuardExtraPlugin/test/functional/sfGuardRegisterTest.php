<?php

include(dirname(__FILE__).'/../bootstrap/functional.php');

$user_data = array(
  'username'      => 'sfGuardRegisterTest'.time(),
  'password'      => 'sfGuardRegisterTest',
  'email_address' => 'sfGuardRegisterTest'.time().'@domain.de',
);

$sf_guard_user = new sfGuardUser();
$sf_guard_user->fromArray($user_data);
$sf_guard_user->save();

$user_data2 = array(
  'username'      => 'sfGuardRegisterTest2'.time(),
  'password'      => 'sfGuardRegisterTest2',
  'email_address' => 'sfGuardRegisterTest2'.time().'@domain.de',
);

$form     = new sfGuardFormRegister();
$formName = $form->getName();

$browser = new sfTestFunctional(new sfBrowser());

$browser->
  info('1. show request')->
  get('/register')->

  with('request')->begin()->
    isParameter('module', 'sfGuardRegister')->
    isParameter('action', 'register')->
  end()->

  with('response')->begin()->
    isValid(true)->
    isStatusCode(200)->
    checkForm($form)->
  end()->

  click('request')->

  with('request')->begin()->
    isParameter('module', 'sfGuardRegister')->
    isParameter('action', 'register')->
  end()->

  with('form')->begin()->
    hasErrors(4)->
    isError('username', 'required')->
    isError('email_address', 'required')->
    isError('password', 'required')->
    isError('password_confirmation', 'required')->
  end()->

  with('response')->begin()->
    isRedirected(false)->
    isStatusCode(200)->
    isValid(true)->
  end()->

  setField($formName.'[username]', $user_data['username'])->
  setField($formName.'[email_address]', 'alpha')->
  setField($formName.'[password]', 'alpha')->
  setField($formName.'[password_confirmation]', 'beta')->
  click('request')->

  with('form')->begin()->
    hasErrors(3)->
    isError('username', 'invalid')->
    isError('email_address', 'invalid')->
    isError('password', 'invalid')->
  end()->

  setField($formName.'[username]', $user_data2['username'])->
  setField($formName.'[email_address]', $user_data['email_address'])->
  setField($formName.'[password]', 'alpha')->
  setField($formName.'[password_confirmation]', 'alpha')->
  click('request')->

  with('form')->begin()->
    hasErrors(1)->
    isError('email_address', 'invalid')->
  end()->

  setField($formName.'[email_address]', $user_data2['email_address'])->
  setField($formName.'[password]', 'alpha')->
  setField($formName.'[password_confirmation]', 'alpha')->
  click('request')->

  info('2. action')->
  with('request')->begin()->
    isParameter('module', 'sfGuardRegister')->
    isParameter('action', 'register')->
  end()->

  with('form')->begin()->
    hasErrors(false)->
  end()->

  with('mailer')->begin()->
    hasSent(1)->
    checkHeader('From', sfConfig::get('app_sf_guard_extra_plugin_from'))->
    checkHeader('Subject', 'Confirm Registration')->
  end()->

  with('response')->begin()->
    isRedirected(true)->
    followRedirect()->
  end()->

  info('3. success page')->
  with('request')->begin()->
    isParameter('module', 'sfGuardRegister')->
    isParameter('action', 'request_confirm_register')->
  end()->

  with('response')->begin()->
    isStatusCode(200)->
    isValid(true)->
  end()->

  info('4. show confirm')->
  get('/register/confirm/'.$sf_guard_user['password'].'/'.$sf_guard_user['id'])->

  with('request')->begin()->
    isParameter('module', 'sfGuardRegister')->
    isParameter('action', 'register_confirm')->
    isParameter('id', $sf_guard_user['id'])->
    isParameter('key', $sf_guard_user['password'])->
  end()->

  with('mailer')->begin()->
    hasSent(1)->
    checkHeader('From', sfConfig::get('app_sf_guard_extra_plugin_from'))->
    checkHeader('Subject', 'Registration Complete')->
  end()->

  with('response')->begin()->
    isRedirected(true)->
    followRedirect()->
  end()->

  with('request')->begin()->
    isParameter('module', 'sfGuardRegister')->
    isParameter('action', 'register_complete')->
  end()->

  with('response')->begin()->
    isStatusCode(200)->
    isValid(true)->
  end()->

  info('5. invalid key')->
  get('/register/confirm/invalidKey/'.$sf_guard_user['id'])->
  with('request')->begin()->
    isParameter('module', 'sfGuardRegister')->
    isParameter('action', 'register_confirm')->
  end()->
  isForwardedTo('sfGuardRegister', 'invalid_key')->

  info('6. check new login')->
  get('/login')->
  setField('signin[username]', $user_data['username'])->
  setField('signin[password]', $user_data['password'])->
  click('sign in')->

  with('user')->begin()->
    isAuthenticated(true)->
  end()->

  info('7. redirect when authenticated')->
  get('/register')->
  with('response')->begin()->
    isRedirected(true)->
  end()
;
