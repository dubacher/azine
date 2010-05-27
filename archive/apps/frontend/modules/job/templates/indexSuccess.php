<h1>Jobs List</h1>
<table>
  <thead>
    <tr>
      <th>Description</th>
      <th>Required skills</th>
      <th>State</th>
      <th>Updated at</th>
    </tr>
  </thead>
  <tbody>
    <?php foreach ($jobs as $job): ?>
    <tr>
      <td><a href="<?php echo url_for('job_show', array('slug' => $job->getSlug())) ?>"><?php echo $job->getDescription() ?></a></td>
      <td><?php echo $job->getRequiredSkills() ?></td>
      <td><?php echo $job->getJobState()->getName() ?></td>
      <td><?php echo $job->getUpdatedAt() ?></td>
    </tr>
    <?php endforeach; ?>
  </tbody>
</table>
