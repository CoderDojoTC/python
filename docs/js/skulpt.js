/* Skulpt embedded Python editor — shared functions for all Skulpt labs */

function outf(text) {
  var el = document.getElementById('output');
  if (el) el.textContent += text;
}

function builtinRead(x) {
  if (Sk.builtinFiles === undefined || Sk.builtinFiles['files'][x] === undefined)
    throw "File not found: '" + x + "'";
  return Sk.builtinFiles['files'][x];
}

function runSkulpt() {
  var target = document.getElementById('turtle-target');
  var output = document.getElementById('output');
  var code   = document.getElementById('code');
  if (!target || !output || !code) return;

  target.innerHTML = '';
  output.textContent = '';

  Sk.pre = 'output';
  Sk.configure({
    output: outf,
    read: builtinRead,
    __future__: Sk.python3,
    killableWhile: true,
    killableFor: true,
  });

  (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'turtle-target';
  Sk.TurtleGraphics.width  = 400;
  Sk.TurtleGraphics.height = 400;

  Sk.misceval.asyncToPromise(function () {
    return Sk.importMainWithBody('<stdin>', false, code.value, true);
  }).catch(function (err) {
    output.textContent = err.toString();
  });
}

function resetSkulpt() {
  var code   = document.getElementById('code');
  var target = document.getElementById('turtle-target');
  var output = document.getElementById('output');
  if (code && window._skulptOriginalCode !== undefined)
    code.value = window._skulptOriginalCode;
  if (target) target.innerHTML = '';
  if (output) output.textContent = '';
}

function _initSkulptEditor() {
  var code = document.getElementById('code');
  if (!code) return;
  window._skulptOriginalCode = code.value;
  code.addEventListener('keydown', function (e) {
    if (e.key === 'Tab') {
      e.preventDefault();
      var s = code.selectionStart;
      code.value = code.value.substring(0, s) + '    ' + code.value.substring(code.selectionEnd);
      code.selectionStart = code.selectionEnd = s + 4;
    }
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', _initSkulptEditor);
} else {
  _initSkulptEditor();
}
