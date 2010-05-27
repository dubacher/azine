<?php

class I18NRequestRoute extends sfRequestRoute
{
  /**
   * Returns true if the URL matches this route, false otherwise.
   *
   * @param  string  $url     The URL
   * @param  array   $context The context
   *
   * @return array   An array of parameters
   */
  public function matchesUrl($url, $context = array())
  {
    $parentResult = parent::matchesUrl($url, $context);
    if(!$parentResult){
      $culture = sfConfig::get('sf_default_culture');
      return parent::matchesUrl("/".$culture.$url, $context);
    }
    return $parentResult;
  }
}
