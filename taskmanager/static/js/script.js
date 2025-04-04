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

    // Timepicker initialisation
    // let timepicker = document.querySelectorAll('.timepicker');
    // M.Timepicker.init(timepicker, {
    //   i18n: {done: "Select"}
    // });

    // Category choice initialisation
    let catChoice = document.querySelectorAll('select');
    M.FormSelect.init(catChoice);

    // Collapsible initialisation
    let collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);
    
    // Modal initialisation
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
  });
