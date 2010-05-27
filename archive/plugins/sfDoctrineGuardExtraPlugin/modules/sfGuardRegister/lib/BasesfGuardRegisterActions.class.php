<?php

/*
 * This file is part of the symfony package.
 * (c) 2004-2006 Fabien Potencier <fabien.potencier@symfony-project.com>
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

/**
 *
 * @package    symfony
 * @subpackage plugin
 * @author     Gordon Franke <gfranke@savedcite.com>
 * @version    SVN: $Id: BasesfGuardRegisterActions.class.php 24814 2009-12-02 20:48:22Z gimler $
 */
class BasesfGuardRegisterActions extends sfActions
{
  /**
   * @see sfAction
   */
  public function preExecute()
  {
    if($this->getUser()->isAuthenticated())
    {
      $this->redirect('@homepage');
    }
  }

  /**
   * Executes register action
   *
   * @param sfWebRequest $request A request object
   *
   * @return void
   */
  public function executeRegister(sfWebRequest $request)
  {
    $this->form = new sfGuardFormRegister();

    if ($request->isMethod('post'))
    {
      $this->form->bind(
        $request->getParameter($this->form->getName()),
        $request->getFiles($this->form->getName())
      );
      if ($this->form->isValid())
      {
        $values = $this->form->getValues();

        $this->form->getObject()->setIsActive(0);
        $sfGuardUser = $this->form->save();

        $this->sendRegisterConfirmMail($sfGuardUser, $values['password']);

        $this->getUser()->setFlash('values', $values);
        $this->getUser()->setFlash('sfGuardUser', $sfGuardUser);

        return $this->redirect('@sf_guard_do_register');
      }
    }
  }

  /**
   * Send the registration confirm email
   *
   * @param object $user     user object
   * @param string $password user password
   *
   * @return void
   */
  public function sendRegisterConfirmMail($user, $password)
  {
    $message = $this->getComponent(
      $this->getModuleName(),
      'send_request_confirm',
      array(
        'sfGuardUser' => $user,
        'password'    => $password
      )
    );

    $this->getMailer()->composeAndSend(
      sfConfig::get('app_sf_guard_extra_plugin_from'),
      $user->getEmailAddress(),
      'Confirm Registration',
      $message
    );
  }

  /**
   * Executes request confirm register action
   *
   * @param sfWebRequest $request A request object
   *
   * @return void
   */
  public function executeRequest_confirm_register(sfWebRequest $request)
  {
  }

  /**
   * Executes register confirm action
   *
   * @param sfWebRequest $request A request object
   *
   * @return void
   */
  public function executeRegister_confirm(sfWebRequest $request)
  {
    $params = array($request->getParameter('key'), $request->getParameter('id'));

    $sfGuardUser = Doctrine_Core::getTable('sfGuardUser')->createQuery('u')
      ->where('u.password = ? AND u.id = ?', $params)
      ->limit(1)
      ->fetchOne();

    $this->forwardUnless($sfGuardUser, 'sfGuardRegister', 'invalid_key');

    $sfGuardUser->setIsActive(1);
    $sfGuardUser->save();

    $this->sendRegisterCompleteMail($sfGuardUser);

    $this->redirect('@sf_guard_register_complete?id='.$sfGuardUser->getId());
  }

  /**
   * Send the registration confirm email
   *
   * @param object $user user object
   *
   * @return void
   */
  public function sendRegisterCompleteMail($user)
  {
    $message = $this->getComponent(
      $this->getModuleName(),
      'send_complete',
      array(
        'sfGuardUser' => $user
      )
    );

    $this->getMailer()->composeAndSend(
      sfConfig::get('app_sf_guard_extra_plugin_from'),
      $user->getEmailAddress(),
      'Registration Complete',
      $message
    );
  }

  /**
   * Executes register complete action
   *
   * @param sfWebRequest $request A request object
   *
   * @return void
   */
  public function executeRegister_complete(sfWebRequest $request)
  {
  }

  /**
   * Executes invalid key action
   *
   * @param sfWebRequest $request A request object
   *
   * @return void
   */
  public function executeInvalid_key(sfWebRequest $request)
  {
  }
}
