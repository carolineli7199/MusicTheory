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
  } else {
    $("#result").append(
      "<div> You have achieved a score of " +
        num +
        "/" +
        total +
        " <br> Come on! Let's do a bit review and try again! </div>"
    );
  }
}
