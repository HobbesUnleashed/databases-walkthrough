document.addEventListener('DOMContentLoaded', function() {
    // SideNav initialisation
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Datepicker initialisation
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mm yyyy",
      i18n: {done: "Select"}
    });

    // Modal initialisation
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);

    // Category choice initialisation
    let catChoice = document.querySelectorAll('select');
    M.FormSelect.init(catChoice);
  });
