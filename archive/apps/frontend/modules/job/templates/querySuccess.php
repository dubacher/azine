<h1>Jobs List</h1>
<div>Query-Form</div>
<div>
<table>
  <thead>
    <tr>
      <th>Id</th>
      <th>State</th>
      <th>User</th>
      <th>Description</th>
      <th>Attachment</th>
      <th>Required skills</th>
      <th>Slug</th>
      <th>Created at</th>
      <th>Updated at</th>
    </tr>
  </thead>
  <tbody>
    <?php foreach ($jobs as $job): ?>
    <tr>
      <td><a href="<?php echo url_for('job_show', array('slug' => $job->getSlug())) ?>"><?php echo $job->getId() ?></a></td>
      <td><?php echo $job->getState() ?></td>
      <td><?php echo $job->getUserId() ?></td>
      <td><?php echo $job->getDescription() ?></td>
      <td><?php echo $job->getAttachment() ?></td>
      <td><?php echo $job->getRequiredSkills() ?></td>
      <td><?php echo $job->getSlug() ?></td>
      <td><?php echo $job->getCreatedAt() ?></td>
      <td><?php echo $job->getUpdatedAt() ?></td>
    </tr>
    <?php endforeach; ?>
  </tbody>
</table>
</div>
  <a href="<?php echo url_for('job_new') ?>">New</a>
