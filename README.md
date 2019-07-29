# Base64 plugin for [Sublime Text](https://www.sublimetext.com)

[![License](https://img.shields.io/github/license/dmitrievav/sublime_base64.svg?style=flat-square)](https://github.com/dmitrievav/sublime_base64/blob/master/LICENSE)
[![Downloads Package Control](https://img.shields.io/packagecontrol/dt/Base64.svg?style=flat-square)](https://packagecontrol.io/packages/Base64)
[![Latest release](https://img.shields.io/github/tag/dmitrievav/sublime_base64.svg)](https://github.com/dmitrievav/sublime_base64/releases/latest)

## Requirements

This plug-in targets and is tested against the **latest Build** of Sublime Text.

* [ST3 (stable)](https://www.sublimetext.com/3)
* [ST3 (dev)](https://www.sublimetext.com/3dev)

This plugin adds commands to base64 decode and encode. If the base64 binary is not in your `$PATH`, you will have to set its location in Preferences → Package Settings → Base64.

![sublime_base64](https://dmitrievav.github.io/gifs/sublime_base64.gif "sublime_base64")

## Installation

Using **Package Control** is not required, but recommended as it keeps your packages (with their dependencies) up-to-date!

### Installation via Package Control

* [Install Package Control](https://packagecontrol.io/installation#st3)
  * Close and reopen Sublime Text after having installed Package Control.
* Open the Command Palette (`Tools > Command Palette`).
* Choose `Package Control: Install Package`.
* Search for [`Base64` on Package Control](https://packagecontrol.io/packages/Base64) and select to install.

In case if this plugin is not available with default `Package Control` channel, you can add repository manually by `Package Control: Add Repository`

<https://raw.githubusercontent.com/dmitrievav/sublime_base64/master/repository.json>

### Manual installation

Download the zip file from the [latest release page](https://github.com/dmitrievav/sublime_base64/releases/latest) and unpack its contents to a subfolder named `Base64` in `../Sublime Text 3/Data/Packages` where Sublime Text 3 is installed.

## Usage

The plug-in's actions are available via the main menu (`Tools → Base64`) or the Command Palette (`Base64: ...`).

### Key bindings

The two main actions of the plug-in are also assigned the following default key bindings:

* decode: "super+b,d"
* encode: "super+b,e"

## Settings

You can use the main menu or the Command Palette to customize the Base64 plug-in's preferences.

## Source code

[github.com/dmitrievav/sublime_base64](https://github.com/dmitrievav/sublime_base64)
