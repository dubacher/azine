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
 * @version    SVN: $Id: BasesfGuardForgotPasswordActions.class.php 25015 2009-12-07 12:55:13Z gimler $
 */
class BasesfGuardForgotPasswordActions extends sfActions
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
   * Executes password action
   *
   * @param sfWebRequest $request A request object
   *
   * @return void
   */
  public function executePassword(sfWebRequest $request)
  {
    $this->form = new sfGuardFormForgotPassword();

    if ($request->isMethod('post'))
    {
      $this->form->bind(
        $request->getParameter($this->form->getName())
      );
      if ($this->form->isValid())
      {
        $values = $this->form->getValues();

        $sfGuardUser = Doctrine_Core::getTable('sfGuardUser')
          ->retrieveByUsernameOrEmailAddress($values['username_or_email_address']);

        $this->sendPasswordMail($sfGuardUser);

        return $this->redirect('@sf_guard_do_password');
      }
    }
  }

  /**
   * Send the request password email to the user
   *
   * @param object $user the user object
   *
   * @return void
   */
  public function sendPasswordMail($user)
  {
    $message = $this->getComponent(
      $this->getModuleName(),
      'send_request_reset_password',
      array(
        'sfGuardUser' => $user,
      )
    );

    $this->getMailer()->composeAndSend(
      sfConfig::get('app_sf_guard_extra_plugin_from'),
      $user->getEmailAddress(),
      'Request to reset password',
      $message
    );
  }

  /**
   * Executes request rest password action
   *
   * @param sfWebRequest $request A request object
   *
   * @return void
   */
  public function executeRequest_reset_password(sfWebRequest $request)
  {
  }

  /**
   * Executes reset password action
   *
   * @param sfWebRequest $request A request object
   *
   * @return void
   */
  public function executeReset_password(sfWebRequest $request)
  {
    $params = array($request->getParameter('key'), $request->getParameter('id'));

    $this->sfGuardUser = Doctrine_Core::getTable('sfGuardUser')
      ->createQuery('u')
      ->where('u.password = ?')
      ->addWhere('u.id = ?')
      ->limit(1)
      ->fetchOne($params);

    $this->forwardUnless($this->sfGuardUser, 'sfGuardForgotPassword', 'invalid_key');

    $newPassword = time();
    $this->sfGuardUser->setPassword($newPassword);
    $this->sfGuardUser->save();

    $this->sendResetPasswordMail($this->sfGuardUser, $newPassword);
  }

  /**
   * Send email to the user with new password
   *
   * @param object $user     user object
   * @param string $password user password
   *
   * @return void
   */
  public function sendResetPasswordMail($user, $password)
  {
    $message = $this->getComponent(
      $this->getModuleName(),
      'send_reset_password',
      array(
        'sfGuardUser' => $user,
        'password' => $password
      )
    );

    $this->getMailer()->composeAndSend(
      sfConfig::get('app_sf_guard_extra_plugin_from'),
      $user->getEmailAddress(),
      'Password reset successfully',
      $message
    );
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
