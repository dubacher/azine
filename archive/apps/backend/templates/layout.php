<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <?php include_http_metas() ?>
    <?php include_metas() ?>
    <?php include_title() ?>
    <link rel="shortcut icon" href="/favicon.ico" />
    <?php include_stylesheets() ?>
    <?php include_javascripts() ?>
    <?php use_stylesheet('admin.css') ?>
  </head>
  <body>
    <div id="container">
      <div id="header">
        <h1>
          Azine Admin Interface
        </h1>
      </div>
      <div id="flash">
        <?php if ($sf_user->hasFlash('notice')): ?>
          <div class="flash_notice">
            <?php echo $sf_user->getFlash('notice') ?>
          </div>
        <?php endif; ?>

        <?php if ($sf_user->hasFlash('error')): ?>
          <div class="flash_error">
            <?php echo $sf_user->getFlash('error') ?>
          </div>
        <?php endif; ?>
      </div>
      <div id="menu">
        <ul>
          <li>
            <?php echo link_to('Jobs', 'job') ?>
          </li>
          <li>
            <?php echo link_to('Applications', 'application') ?>
          </li>
          <li>
            <?php echo link_to('sfGuardUsers', 'sf_guard_user') ?>
          </li>
          <li>
            <?php echo link_to('JobStates', 'job_state') ?>
          </li>
        </ul>
      </div>
      <div id="content">
        <?php echo $sf_content ?>
      </div>

    </div>
  </body>
</html>