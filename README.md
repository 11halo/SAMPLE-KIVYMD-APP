# SAMPLE-KIVYMD-APP
name: CI
on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      # used to cache dependencies with a timeout
      - name: Get Date
        id: get-date
        run: |
          echo "::set-output name=date::$(/bin/date -u "+%Y%m%d")"
        shell: bash

      - name: Cache Buildozer global directory
        uses: actions/cache@v2
        with:
          path: .buildozer_global
          key: buildozer-global-${{ hashFiles('buildozer.spec') }} # Replace with your path

      - uses: actions/cache@v2
        with:
          path: .buildozer
          key: ${{ runner.os }}-${{ steps.get-date.outputs.date }}-${{ hashFiles('buildozer.spec') }}

      - name: Build with Buildozer
        uses: ArtemSBulgakov/buildozer-action@v1
        id: buildozer
        with:
          command: buildozer android debug
          buildozer_version: master

      - name: Upload artifacts
        uses: actions/upload-artifact@v2
        with:
          name: package
          path: ${{ steps.buildozer.outputs.filename }}
