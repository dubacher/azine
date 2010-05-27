<?php

/**
 * job actions.
 *
 * @package    azine
 * @subpackage job
 * @author     DominikBusinger
 * @version    SVN: $Id: actions.class.php 23810 2009-11-12 11:07:44Z Kris.Wallsmith $
 */
class jobActions extends sfActions
{
  public function executeIndex(sfWebRequest $request)
  {
    $this->jobs = Doctrine::getTable('Job')
      ->createQuery('a')
      ->execute();
  }

  public function executeShow(sfWebRequest $request)
  {
    $this->job = JobTable::findJobBySlug($request->getParameter('slug'));
    $this->editable = $this->getUser() == $this->job->getUser();
    if(true || $this->editable){
    	$this->applications = ApplicationTable::getApplicationsForJob($this->job);
    }
  }

  public function executeNew(sfWebRequest $request)
  {
    $this->form = new AzineJobForm();
    
    if ($request->isMethod('post') || $request->isMethod('put')){
      // set the current user as author
      $taintedValues = $request->getParameter($this->form->getName());
      $this->processForm($request, $this->form);
    }

    $this->setTemplate('new');
  }

  public function executeUpdate(sfWebRequest $request)
  {
    $job = JobTable::findJobBySlug($request->getParameter('slug'));
    $this->forward404Unless($job, sprintf('Object job does not exist (%s).', $request->getParameter('slug')));
    $this->form = new AzineJobForm($job);

    if ($request->isMethod('post') || $request->isMethod('put')){
      $this->processForm($request, $this->form);
    }

  }

  public function executeDelete(sfWebRequest $request)
  {
    $request->checkCSRFProtection();

    $job = JobTable::findJobBySlug($request->getParameter('slug'));
    $this->forward404Unless($job, sprintf('Object job does not exist (%s).', $request->getParameter('slug')));
    $job->delete();

    $this->redirect('jobs');
  }
  
  protected function processQuery(sfWebRequest $request, sfForm $form)
  {
  	// create query from request-parameters.
    $this->jobs = Doctrine::getTable('Job')
      ->createQuery('a')
      ->execute();
  }
  
  protected function processForm(sfWebRequest $request, sfForm $form)
  {
    // set the current user as author of the tip.
    $taintedValues = $request->getParameter($form->getName());
    $taintedValues['user_id'] = $this->getUser()->getGuardUser()->getId();

    $form->bind($taintedValues, $request->getFiles($form->getName()));
    if ($form->isValid())
    {
      $job = $form->save();
      
      $this->getUser()->setFlash('notice', 'The job has been saved.');

      $this->redirect('job_show', array('slug' => $job->getSlug()));
    }
  }
}
