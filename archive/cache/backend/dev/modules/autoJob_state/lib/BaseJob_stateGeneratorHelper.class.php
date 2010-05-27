<?php

/**
 * job_state module configuration.
 *
 * @package    ##PROJECT_NAME##
 * @subpackage job_state
 * @author     ##AUTHOR_NAME##
 * @version    SVN: $Id: helper.php 24171 2009-11-19 16:37:50Z Kris.Wallsmith $
 */
abstract class BaseJob_stateGeneratorHelper extends sfModelGeneratorHelper
{
  public function getUrlForAction($action)
  {
    return 'list' == $action ? 'job_state' : 'job_state_'.$action;
  }
}
