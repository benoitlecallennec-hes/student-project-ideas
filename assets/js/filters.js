// Filtrage client de la liste des sujets : OU à l'intérieur d'un groupe,
// ET entre les groupes. L'état est reflété dans l'URL pour être partageable.
(function () {
  var bar = document.getElementById("project-filters");
  var list = document.getElementById("project-list");
  if (!bar || !list) return;

  var GROUPS = { cats: "cat", stat: "stat" };
  var items = Array.prototype.slice.call(list.querySelectorAll(".pi"));
  var chips = Array.prototype.slice.call(bar.querySelectorAll(".pf-chip"));
  var empty = document.getElementById("project-empty");
  var counter = document.getElementById("project-count");
  var reset = document.getElementById("pf-reset");
  var selected = { cats: [], stat: [] };

  function values(item, group) {
    var raw = item.getAttribute(group === "cats" ? "data-cats" : "data-stat") || "";
    return raw ? raw.split("|") : [];
  }

  function matches(item, group) {
    if (!selected[group].length) return true;
    var own = values(item, group);
    for (var i = 0; i < own.length; i++) {
      if (selected[group].indexOf(own[i]) !== -1) return true;
    }
    return false;
  }

  function render() {
    var shown = 0;
    items.forEach(function (item) {
      var visible = matches(item, "cats") && matches(item, "stat");
      item.classList.toggle("is-hidden", !visible);
      if (visible) shown++;
    });

    chips.forEach(function (chip) {
      var on = selected[chip.dataset.group].indexOf(chip.dataset.value) !== -1;
      chip.classList.toggle("is-on", on);
      chip.setAttribute("aria-pressed", on ? "true" : "false");
    });

    if (empty) empty.classList.toggle("is-hidden", shown !== 0);

    if (counter) {
      var total = counter.dataset.total;
      // En français 0 et 1 prennent le singulier.
      var tpl = shown <= 1 ? counter.dataset.tplOne : counter.dataset.tplMany;
      counter.textContent = tpl.replace("{n}", shown).replace("{total}", total);
    }

    var params = new URLSearchParams();
    Object.keys(GROUPS).forEach(function (group) {
      selected[group].forEach(function (v) {
        params.append(GROUPS[group], v);
      });
    });
    var query = params.toString();
    history.replaceState(null, "", query ? "?" + query : location.pathname);
  }

  function toggle(group, value) {
    var at = selected[group].indexOf(value);
    if (at === -1) selected[group].push(value);
    else selected[group].splice(at, 1);
    render();
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      toggle(chip.dataset.group, chip.dataset.value);
    });
  });

  if (reset) {
    reset.addEventListener("click", function () {
      selected = { cats: [], stat: [] };
      render();
    });
  }

  var known = { cats: [], stat: [] };
  chips.forEach(function (chip) {
    known[chip.dataset.group].push(chip.dataset.value);
  });

  var incoming = new URLSearchParams(location.search);
  Object.keys(GROUPS).forEach(function (group) {
    incoming.getAll(GROUPS[group]).forEach(function (v) {
      // Une valeur inconnue viendrait d'un lien obsolète : on l'ignore.
      if (known[group].indexOf(v) !== -1 && selected[group].indexOf(v) === -1) {
        selected[group].push(v);
      }
    });
  });

  bar.removeAttribute("hidden");
  render();
})();
