/* Skulpt embedded Python editor — shared functions for all Skulpt labs.
 *
 * Single-lab pages use the default IDs (no suffix):
 *   id="code"  id="output"  id="turtle-target"  etc.
 *   Buttons: onclick="runSkulpt()"   onclick="resetSkulpt()"
 *
 * Pages with multiple labs give each additional lab a suffix, e.g. "-2":
 *   id="code-2"  id="output-2"  id="turtle-target-2"  etc.
 *   Buttons: onclick="runSkulpt('-2')"   onclick="resetSkulpt('-2')"
 */

function builtinRead(x) {
  if (Sk.builtinFiles === undefined || Sk.builtinFiles['files'][x] === undefined)
    throw "File not found: '" + x + "'";
  return Sk.builtinFiles['files'][x];
}

function runSkulpt(suffix) {
  suffix = suffix || '';
  var target = document.getElementById('turtle-target' + suffix);
  var output = document.getElementById('output' + suffix);
  var code   = document.getElementById('code' + suffix);
  if (!target || !output || !code) return;

  target.innerHTML  = '';
  output.textContent = '';
  output.classList.remove('skulpt-error');

  Sk.configure({
    output: function (text) { output.textContent += text; },
    read:   builtinRead,
    __future__:   Sk.python3,
    killableWhile: true,
    killableFor:   true,
  });

  (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'turtle-target' + suffix;
  Sk.TurtleGraphics.width  = 400;
  Sk.TurtleGraphics.height = 400;

  Sk.misceval.asyncToPromise(function () {
    return Sk.importMainWithBody('<stdin>', false, code.value, true);
  }).catch(function (err) {
    output.textContent = err.toString();
    output.classList.add('skulpt-error');
  });
}

function resetSkulpt(suffix) {
  suffix = suffix || '';
  var code   = document.getElementById('code' + suffix);
  var target = document.getElementById('turtle-target' + suffix);
  var output = document.getElementById('output' + suffix);
  var key    = '_skulptOriginalCode' + suffix;
  if (code   && window[key] !== undefined) code.value = window[key];
  if (target) target.innerHTML   = '';
  if (output) output.textContent = '';
}

function _initSkulptEditor() {
  /* Initialise every textarea whose id is "code" or starts with "code-". */
  document.querySelectorAll('textarea[id="code"], textarea[id^="code-"]').forEach(function (code) {
    var suffix = (code.id === 'code') ? '' : code.id.slice(4); /* "code-2" → "-2" */
    window['_skulptOriginalCode' + suffix] = code.value;

    /* Auto-size the textarea to show all initial code without scrolling.
       Trim trailing newlines so the blank line before </textarea> in the
       markdown source doesn't add an empty row, then let the browser measure
       the exact pixel height via scrollHeight rather than estimating per-line.
       scrollHeight excludes borders; +4 compensates for the 2 px top+bottom
       border under box-sizing: border-box. */
    var saved = code.value;
    code.value = code.value.replace(/\n+$/, '');
    code.style.height = '0px';
    code.style.height = Math.max(120, code.scrollHeight + 4) + 'px';
    code.value = saved;

    code.addEventListener('keydown', function (e) {
      if (e.key === 'Tab') {
        e.preventDefault();
        var s = code.selectionStart;
        code.value = code.value.substring(0, s) + '    ' + code.value.substring(code.selectionEnd);
        code.selectionStart = code.selectionEnd = s + 4;
      }
    });
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', _initSkulptEditor);
} else {
  _initSkulptEditor();
}
