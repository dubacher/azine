<?php

/**
 * Content actions.
 *
 * @package    azine
 * @subpackage Content
 * @author     DominikBusinger
 * @version    SVN: $Id: actions.class.php 23810 2009-11-12 11:07:44Z Kris.Wallsmith $
 */
class sfGuardSettingsActions extends sfActions
{
 /**
  * Executes user settings action
  *
  * @param sfRequest $request A request object
  */
  public function executeSettings(sfWebRequest $request)  {
	$this->form = new AzineUserForm($this->getUser()->getGuardUser());

	if ($request->isMethod('post') || $request->isMethod('put')){
      $this->processForm($request, $this->form);
    }
	
  }
  
  protected function processForm(sfWebRequest $request, sfForm $form)
  {
    $form->bind($taintedValues, $request->getFiles($form->getName()));
    if ($form->isValid())
    {
      $job = $form->save();
      
      $this->getUser()->setFlash('notice', 'Your settings have been saved.');

      $this->redirect('@welcome', array());
    } else {
      $this->getUser()->setFlash('error', 'Your settings could not be saved.');
    }
  }
  
  
 /**
  * Executes unregister user action
  *
  * @param sfRequest $request A request object
  */
  public function executeUnregister(sfWebRequest $request)  {

  }
  
}
