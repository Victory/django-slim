jQuery(function($) {
  var bindInfoTip = function () {
    $("#infoTipForm button").click(function (evt) {
      evt.preventDefault();
      $.post(
        infoTipFormUrl,
        $("#infoTipForm").serialize(),
        function (data, status, xhr) {
          if (!data.success) {
            $("#infoTipForm").html(data.html);
            bindInfoTip();
          } else {
            $("#infoTipForm").html("Thanks for Submitting!");
          }
        });
    });
  };
  bindInfoTip();
});
