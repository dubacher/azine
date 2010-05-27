<td class="sf_admin_text sf_admin_list_td_id">
  <?php echo link_to($application->getId(), 'application_edit', $application) ?>
</td>
<td class="sf_admin_foreignkey sf_admin_list_td_job_id">
  <?php echo $application->getJobId() ?>
</td>
<td class="sf_admin_foreignkey sf_admin_list_td_applicant_id">
  <?php echo $application->getApplicantId() ?>
</td>
<td class="sf_admin_text sf_admin_list_td_requested_rate">
  <?php echo $application->getRequestedRate() ?>
</td>
<td class="sf_admin_text sf_admin_list_td_rate_type">
  <?php echo $application->getRateType() ?>
</td>
<td class="sf_admin_text sf_admin_list_td_application_text">
  <?php echo $application->getApplicationText() ?>
</td>
<td class="sf_admin_text sf_admin_list_td_cv_attachment">
  <?php echo $application->getCvAttachment() ?>
</td>
<td class="sf_admin_date sf_admin_list_td_created_at">
  <?php echo false !== strtotime($application->getCreatedAt()) ? format_date($application->getCreatedAt(), "f") : '&nbsp;' ?>
</td>
<td class="sf_admin_date sf_admin_list_td_updated_at">
  <?php echo false !== strtotime($application->getUpdatedAt()) ? format_date($application->getUpdatedAt(), "f") : '&nbsp;' ?>
</td>
