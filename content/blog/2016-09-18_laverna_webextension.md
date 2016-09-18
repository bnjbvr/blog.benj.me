Title: Laverna Webclipper, the story of a WebExtension
Date: 2016-09-18 17:10
Author: Benjamin Bouvier
Lang: en
Tags: opensource
Slug: laverna-webclipper-webextension

Yesterday I've spent my afternoon on a very small side-project related to
[Laverna](https://laverna.cc/app).

Laverna is an offline-first, no-backend Web application that allows you to
write notes directly from your browser, classify them in notebooks, with a
live-preview Markdown editor and a powerful yet simple tagging system. Besides
being offline-first, it also allows you to sync between different devices,
using [Dropbox](http://dropbox.github.io/dropbox-sdk-js/) as a backend or your
own instance of a [RemoteStorage](https://remotestorage.io/) server. All of
this makes it a powerful free and open-source alternative to software like
[Evernote](http://www.evernote.com/) or even [Microsoft
OneNote](http://www.onenote.com/).

## A WebClipper for Laverna

There was already an official
[webclipper](https://github.com/laverna/webclipper), but when I've tried it, it
didn't work. Looking at the code and the last commit date, it seemed a bit
deprecated; so I made my own that uses WebExtensions (since I really wanted to
learn a bit more about these), that you can find [here on
Github](https://github.com/bnjbvr/laverna-webclipper).

The idea behind a web clipper is very simple: you go on a Web page that
contains some interesting content and you would like to keep it for later (for
example, to read it later, or to keep it as reference). So the addon
introduces a new click button in the browser bar that opens a new Laverna tab
and prefills the field with the parsed content, one-click away from being
saved. This is useful because some read-it-later services can't have access to
content behind paid-walls, for instance.

[See it in action here.](https://benj.me/pub/demo-laverna-webclipper.webm)

If you're interested in getting this addon, you can go on the [official addons
for Firefox
website](https://addons.mozilla.org/en-US/firefox/addon/laverna-clipper/) (as
of the day of this writing, the addon has not been validated yet).

## The Implementation

This project is using [Readability.js](https://github.com/mozilla/readability)
for retrieving the "interesting content" of a page, and then renders it to
Markdown (since Laverna uses this format) thanks to
[html.md](https://github.com/neocotic/html.md). The rest is plumbing :)

[WebExtensions](https://wiki.mozilla.org/WebExtensions) are a new safe and
portable way to write addons for Web browsers. Heavily inspired from Chrome's
Addons APIs, the main thrust is that WebExtensions should Just Work© on any Web
browser supporting them (any Chromium-based, Edge and Firefox, as of today).

This is fantastic news! ... when all the browsers will support it. As of today,
this addon will only work on Firefox, and here is why.

First, programming a WebExtension is *hard*. I mean **really** hard; debugging
it may quickly become a nightmare, because debug messages can appear in the
developer console (for the content script, which is the "client" part of your
addon), or in a specific addon debugger console (for background scripts), or
even in the `stdout` logs of your browser. Some issues, like parsing errors in
your JavaScript files, may be really hard to find in this context.

Second, at some point in the addon's workflow, you need to inject the Markdown
content into the Laverna's text editor. Laverna uses
[CodeMirror](http://codemirror.net/) for their rich text editor, so dumping the
content is not just as simple as setting the `value` property of the target
`textarea`. You need to retrieve the CodeMirror instance somehow and call one of its
methods. The instance is fortunately saved in the
`.CodeMirror` property of the textarea, so you could retrieve it, if you really
were on the client page. But browsers don't
[allow](https://developer.chrome.com/extensions/content_scripts#execution-environment)
[that](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Content_scripts#Xray_vision_in_Firefox),
unless modifying the observed page itself, which I didn't know about when writing this addon.

That being said, Firefox gives you a (hacky) way to do so (through
`wrappedJSObject`), so you can indeed access the original JS DOM object of the
observed page and retrieve the CodeMirror instance, then call its `setValue`
method. Pfew! Chrome doesn't have this hack, which is merely the reason why it
doesn't work there.

Unrelated to these issues: whenever one clicks on the clipper button, the page
is parsed, which has the unfortunate side-effect of clearing the parsed content
(that's how Readability works). One can clone the entire DOM to prevent this
issue, but this API is not (yet?) available in WebExtensions, at least under
Firefox. To work around this, the page is reloaded in the background after
you've clicked the button. Filthy, right?

## Get in touch!

If you have any remarks or suggestions, don't hesitate to ping me on
[twitter](https://twitter.com/bnjbvr/) or
[diaspora](https://framasphere.org/people/315a5640ead10132c4cc2a0000053625); I
love any kind of feedback, since this is usually the only way to get better and
understand what matters. If you're interested in contributing to this addon,
let's get in touch!
