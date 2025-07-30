/* Replace alert boxes to avoid rendering issues */
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('div.alert.alert-warning').forEach(el => {
    // Remove old classes
    el.classList.remove('alert', 'alert-warning');
    // Add your new class
    el.classList.add('exercise-block');
  });
});

