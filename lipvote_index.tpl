%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<link rel="stylesheet" type="text/css" href="lipvote_index.css" />
<link href='http://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>

<h1>LipVote!</h1>
<p>Add sum sick beats up in this heezy:</p>
<form action="/new" method="GET">
Choon: <input type="text" size="20" maxlength="50" name="choon">
Artist: <input type="text" size="20" maxlength="50" name="artist">
<input type="submit" name="save" value="save">
</form>
<p>The phat choons that may involve some lipping are listed below:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>