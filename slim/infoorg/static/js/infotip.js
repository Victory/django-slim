jQuery(function($) {
  var bindInfoTip = function () {
    $("#infoTipForm button").click(function (evt) {
      evt.preventDefault();
      $.post(
        infoTipFormUrl,
        $("#infoTipForm").serialize(),
        function (data, status, xhr) {
          if (!data.success) {
            $("#formBox").html(data.html);
            bindInfoTip();
          } else {
            $("#formBox").html("Thanks for Submitting!");
          }
        });
    });
  };
  bindInfoTip();
});
