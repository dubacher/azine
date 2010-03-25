<?php use_stylesheets_for_form($form) ?>
<?php use_javascripts_for_form($form) ?>
<form
    action="<?php echo url_for('sf_guard_settings') ?>"
    method="post"
    <?php $form->isMultipart() and print 'enctype="multipart/form-data" ' ?>>
  <table>
    <tfoot>
      <tr>
        <td colspan="2">
          <?php echo $form->renderHiddenFields(false) ?>
          <?php 
              echo link_to(__('Cancel'), '@homepage');
              echo "&nbsp;";
              echo link_to(__('Unregister'), '@sf_guard_unregister');
           ?>
          <input type="submit" value="Save" />
        </td>
      </tr>
    </tfoot>
    <tbody>
	<?php echo $form; ?>
    </tbody>
  </table>
</form>


