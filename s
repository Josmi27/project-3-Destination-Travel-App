[1mdiff --cc templates/about.html[m
[1mindex 66f7151,49b1abe..0000000[m
[1m--- a/templates/about.html[m
[1m+++ b/templates/about.html[m
[36m@@@ -11,7 -11,7 +11,11 @@@[m
          <font color="#e5a56f"><strong>[m
              <ul>[m
                  <li>Joy Elias - Computer Science Senior at Morgan State University[m
[32m++<<<<<<< HEAD[m
[32m +                <br><em>Fun fact: I've traveled to Mexico 4 times.</em></li>[m
[32m++=======[m
[32m+                 <br><em>Fun fact:</em></li>[m
[32m++>>>>>>> b9445c7146dba1239a21af6b1676d2fdc7bf0812[m
  [m
                  <br><li>Morgan Whitaker - Computer Science Senior at Morgan State University[m
                  <br><em>Fun fact: </em>        [m
[36m@@@ -25,29 -25,23 +29,41 @@@[m
  [m
          <br>[m
          <span style="text-decoration: underline;">WHAT HAVE WE MADE? WHAT DOES IT EVEN DO?</span>[m
[31m-         <br><font color="#e5a56f"><strong>We have made a real-time chat app accessible [m
[32m+         <br><ul><font color="#e5a56f"><strong><li>We have made a real-time chat app accessible [m
          from the browser. The chat app <br>will provide a social login to allow users to easily [m
[31m-         identify themselves, and feature an international chatbot with a friendly attitude, [m
[31m-         which enables users to do tasks like book flights and hotels. </strong></font>[m
[32m+         identify themselves, and feature <br>an international chatbot with a friendly attitude, [m
[32m+         which enables users to do tasks like <br>book flights and hotels. </li></strong></font></ul>[m
          [m
          <br><span style="text-decoration: underline;">HOW DID WE MAKE IT? (Technologies Included)</span>[m
[32m++<<<<<<< HEAD[m
[32m +        <br><font color="blue"><strong> To create this chat app, we utilized AWS Cloud9 as environment to test and create out code.[m
[32m +        We used Flask for the backend of our site and React/JS for the front-end, tied in with SocketIO. To expand on the features of our application[m
[32m +        we pulled in multiple APIs: Genius Music, Currency Converter-5, My Memory API, Cometari Airport Finder, Reisewarnung API, and Trail API. These[m
[32m +        APIs allowed us to access music, airport names, travel advisories, currency conversions, activities and more. We stored our code on a [m
[32m +        group repository on Github. </strong></font>[m
[32m +        <span style="text-decoration: underline;">WHAT WAS THE MOTIVATION?</span>[m
[32m +        <br>[m
[32m +        <span style="text-decoration: underline;">WHY DOES IT MATTER?</span>[m
[32m +        <br><font color="blue"><strong>As Computer Science students heading into industry in the coming months, it was important that we[m
[32m +        understood all that need to go into creating a complex application. When creating a project, it is important to know who and what you are[m
[32m +        are making it for to make sure that all possible needs and wants are taken care of. Creating this chat app, with a theme focused on travel,[m
[32m +        helped us learn how to manuever around the "wants" of the customer and to put out a product that worked and would make people happy. Using this[m
[32m +        travel theme allowed us to think about what people would actually want to see in an application and what features needed to to create a great app. [m
[32m +        This project helped us experience a lot of what we will be experiencing as we enter into industry. </strong></font>[m
[32m +        <span style="text-decoration: underline;">WHERE CAN YOU GO TO CHECK THIS OUT?</span>●[m
[32m++=======[m
[32m+         <br>[m
[32m+         <br><span style="text-decoration: underline;">WHAT WAS THE MOTIVATION?</span>[m
[32m+         <br>[m
[32m+         <ul><font color="blue"><strong><li>We wanted to demonstrate and apply the core concepts used in our COSC 458 course [m
[32m+         by <br>exploring the potential capabilities of a complex chatbot, within an [m
[32m+         international communication <br>app.</li></strong></font></ul>[m
[32m+         <br><br><span style="text-decoration: underline;">WHY DOES IT MATTER?</span>[m
[32m+         <br>[m
[32m+         <br><span style="text-decoration: underline;">WHERE CAN YOU GO TO CHECK THIS OUT?</span>[m
[32m++>>>>>>> b9445c7146dba1239a21af6b1676d2fdc7bf0812[m
          <ul>[m
[31m-             <li>It's all right here -> http://frozen-crag-41604.herokuapp.com/</li>[m
[32m+             <li><strong><font color="black">It's all right here -> <a href="http://frozen-crag-41604.herokuapp.com/">Click me!</a></strong></font></li>[m
          </ul>[m
          </p>[m
          <script type="text/javascript" src="/static/script.js"></script>[m
