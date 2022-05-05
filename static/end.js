$(document).ready(function () {
  loadQuizEnd(num, total);
});

function loadQuizEnd(num, total) {
  console.log(num);
  if (num > total * 0.7) {
    $("#result").append(
      "<div>  Congratulations! You have passed with a score of " +
        num +
        "/" +
        total +
        " </div>"
    );
    $("#previous-button").html(
      "<a href='/'> <button class='next-button-start'>" +
        "<span lass='next-button-wrapper'>  Home  </span></button></a>"
    );
  } else {
    $("#result").append(
      "<div> You have achieved a score of " +
        num +
        "/" +
        total +
        " <br> Let's do a bit review and try again! </div>"
    );
    $("#previous-button").html(
      "<a href='/learning/1'> <button class='next-button-start'>" +
        "<span lass='next-button-wrapper'>  Review  </span></button></a>"
    );
  }
}
