<?php

/**
 * application actions.
 *
 * @package    azine
 * @subpackage application
 * @author     DominikBusinger
 * @version    SVN: $Id: actions.class.php 23810 2009-11-12 11:07:44Z Kris.Wallsmith $
 */
class applicationActions extends sfActions
{
//  public function executeIndex(sfWebRequest $request)
//  {
//    $this->applications = Doctrine::getTable('Application')
//      ->createQuery('a')
//      ->execute();
//  }
//
//  public function executeNew(sfWebRequest $request)
//  {
//    $this->form = new ApplicationForm();
//  }
//
//  public function executeCreate(sfWebRequest $request)
//  {
//    $this->forward404Unless($request->isMethod(sfRequest::POST));
//
//    $this->form = new ApplicationForm();
//
//    $this->processForm($request, $this->form);
//
//    $this->setTemplate('new');
//  }
//
//  public function executeEdit(sfWebRequest $request)
//  {
//    $this->forward404Unless($application = Doctrine::getTable('Application')->find(array($request->getParameter('id'))), sprintf('Object application does not exist (%s).', $request->getParameter('id')));
//    $this->form = new ApplicationForm($application);
//  }
//
//  public function executeUpdate(sfWebRequest $request)
//  {
//    $this->forward404Unless($request->isMethod(sfRequest::POST) || $request->isMethod(sfRequest::PUT));
//    $this->forward404Unless($application = Doctrine::getTable('Application')->find(array($request->getParameter('id'))), sprintf('Object application does not exist (%s).', $request->getParameter('id')));
//    $this->form = new ApplicationForm($application);
//
//    $this->processForm($request, $this->form);
//
//    $this->setTemplate('edit');
//  }
//
//  public function executeDelete(sfWebRequest $request)
//  {
//    $request->checkCSRFProtection();
//
//    $this->forward404Unless($application = Doctrine::getTable('Application')->find(array($request->getParameter('id'))), sprintf('Object application does not exist (%s).', $request->getParameter('id')));
//    $application->delete();
//
//    $this->redirect('application/index');
//  }
//
//  protected function processForm(sfWebRequest $request, sfForm $form)
//  {
//    $form->bind($request->getParameter($form->getName()), $request->getFiles($form->getName()));
//    if ($form->isValid())
//    {
//      $application = $form->save();
//
//      $this->redirect('application/edit?id='.$application->getId());
//    }
//  }

  /**
   * 
   * @param sfWebRequest $request
   * @return unknown_type
   */
  public function executeApply(sfWebRequest $request){
  }
  
  /**
   * 
   * @param sfWebRequest $request
   * @return unknown_type
   */
  public function executeManageApplications(sfWebRequest $request){
  }

  /**
   * 
   * @param sfWebRequest $request
   * @return unknown_type
   */
  public function executeReply(sfWebRequest $request){
  }

  /**
   * 
   * @param sfWebRequest $request
   * @return unknown_type
   */
  public function executeDecline(sfWebRequest $request){
  }

}
