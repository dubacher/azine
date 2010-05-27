<?php

class sfGuardUserTable extends PluginsfGuardUserTable
{

    public function retrieveByUsernameOrEmailAddress($usernameOrEmail, $isActive = true)
    {
      return $this->createQuery('u')
        ->where('u.username = ? OR u.email_address = ?')
        ->addWhere('u.is_active = ?')
        ->fetchOne(array(
            $usernameOrEmail,
            $usernameOrEmail,
            $isActive
          )
        );
    }

}
