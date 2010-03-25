<?php use_stylesheets_for_form($form) ?>
<?php use_javascripts_for_form($form) ?>

<form action="<?php echo url_for('application/'.($form->getObject()->isNew() ? 'create' : 'update').(!$form->getObject()->isNew() ? '?id='.$form->getObject()->getId() : '')) ?>" method="post" <?php $form->isMultipart() and print 'enctype="multipart/form-data" ' ?>>
<?php if (!$form->getObject()->isNew()): ?>
<input type="hidden" name="sf_method" value="put" />
<?php endif; ?>
  <table>
    <tfoot>
      <tr>
        <td colspan="2">
          <?php echo $form->renderHiddenFields(false) ?>
          &nbsp;<a href="<?php echo url_for('application/index') ?>">Back to list</a>
          <?php if (!$form->getObject()->isNew()): ?>
            &nbsp;<?php echo link_to('Delete', 'application/delete?id='.$form->getObject()->getId(), array('method' => 'delete', 'confirm' => 'Are you sure?')) ?>
          <?php endif; ?>
          <input type="submit" value="Save" />
        </td>
      </tr>
    </tfoot>
    <tbody>
      <?php echo $form->renderGlobalErrors() ?>
      <tr>
        <th><?php echo $form['job_id']->renderLabel() ?></th>
        <td>
          <?php echo $form['job_id']->renderError() ?>
          <?php echo $form['job_id'] ?>
        </td>
      </tr>
      <tr>
        <th><?php echo $form['applicant_id']->renderLabel() ?></th>
        <td>
          <?php echo $form['applicant_id']->renderError() ?>
          <?php echo $form['applicant_id'] ?>
        </td>
      </tr>
      <tr>
        <th><?php echo $form['requested_rate']->renderLabel() ?></th>
        <td>
          <?php echo $form['requested_rate']->renderError() ?>
          <?php echo $form['requested_rate'] ?>
        </td>
      </tr>
      <tr>
        <th><?php echo $form['rate_type']->renderLabel() ?></th>
        <td>
          <?php echo $form['rate_type']->renderError() ?>
          <?php echo $form['rate_type'] ?>
        </td>
      </tr>
      <tr>
        <th><?php echo $form['application_text']->renderLabel() ?></th>
        <td>
          <?php echo $form['application_text']->renderError() ?>
          <?php echo $form['application_text'] ?>
        </td>
      </tr>
      <tr>
        <th><?php echo $form['cv_attachment']->renderLabel() ?></th>
        <td>
          <?php echo $form['cv_attachment']->renderError() ?>
          <?php echo $form['cv_attachment'] ?>
        </td>
      </tr>
      <tr>
        <th><?php echo $form['created_at']->renderLabel() ?></th>
        <td>
          <?php echo $form['created_at']->renderError() ?>
          <?php echo $form['created_at'] ?>
        </td>
      </tr>
      <tr>
        <th><?php echo $form['updated_at']->renderLabel() ?></th>
        <td>
          <?php echo $form['updated_at']->renderError() ?>
          <?php echo $form['updated_at'] ?>
        </td>
      </tr>
    </tbody>
  </table>
</form>
