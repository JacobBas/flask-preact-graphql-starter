// IMPORTS
import * as _Preact from "https://cdn.skypack.dev/preact@10.4.7";
import * as _Hooks from "https://cdn.skypack.dev/preact@10.4.7/hooks";
import htm from "https://cdn.skypack.dev/htm@3.0.4";
import "https://cdnjs.cloudflare.com/ajax/libs/uuid/8.1.0/uuidv4.min.js";

// EXPORTS
export const html = htm.bind(_Preact.h);
export const Preact = _Preact;
export const Hooks = _Hooks;

// PAGE FUNCTION
const Page = () => {
	return html`Hello there!`
}

// RENDERING THE PAGE
_Preact.render(html`<${Page} />`, document.getElementById("root"))
