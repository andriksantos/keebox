---
title: "Mobile Development – Curated Developer Resources"
description: "Curated cross-platform and Android development frameworks, UI libraries, tools and learning resources for building mobile apps."
---

# Mobile Development

Curated cross-platform and Android development frameworks, UI libraries, tools and learning resources for building mobile apps.

!!! tip "28 hand-picked resources"
    Every link on this page was checked in November 2026. Know a great project that is missing? [Suggest it on GitHub](https://github.com/andriksantos/keebox/issues/new) or read the [contribution guide](contributing.md).

## Cross-platform frameworks

- [Flutter](https://github.com/flutter/flutter) - Google's UI toolkit for mobile, web and desktop from a single codebase.
- [React Native](https://github.com/react/react-native) - Build native apps using React.
- [Expo](https://github.com/expo/expo) - Framework and platform for universal React applications.
- [Ionic](https://github.com/ionic-team/ionic-framework) - Build mobile and desktop apps with web technologies.
- [Capacitor](https://github.com/ionic-team/capacitor) - Build cross-platform native web apps.
- [Kotlin Multiplatform samples](https://github.com/Kotlin/kmp-production-sample) - Production-ready sample of a Kotlin Multiplatform app.
- [Compose Multiplatform](https://github.com/JetBrains/compose-multiplatform) - Declarative UI framework for Android, iOS, desktop and web.
- [Tauri](https://github.com/tauri-apps/tauri) - Build smaller, faster and more secure desktop and mobile apps.

## Android

- [Now in Android](https://github.com/android/nowinandroid) - Fully functional Android app built with Kotlin and Jetpack Compose.
- [Android architecture samples](https://github.com/android/architecture-samples) - Samples that showcase architecture approaches.
- [Retrofit](https://github.com/lysine-dev/retrofit) - Type-safe HTTP client for Android and Java.
- [OkHttp](https://github.com/lysine-dev/okhttp) - Square's meticulous HTTP client.
- [Coil](https://github.com/coil-kt/coil) - Image loading for Android and Compose Multiplatform.
- [LeakCanary](https://github.com/square/leakcanary) - Memory leak detection library for Android.

## Flutter & React Native libraries

- [Riverpod](https://github.com/rrousselGit/riverpod) - Reactive caching and data-binding framework for Flutter.
- [flutter_bloc](https://github.com/felangel/bloc) - Predictable state management library for Dart.
- [React Navigation](https://github.com/react-navigation/react-navigation) - Routing and navigation for React Native apps.
- [React Native Reanimated](https://github.com/software-mansion/react-native-reanimated) - Smooth animations and interactions for React Native.
- [NativeWind](https://github.com/nativewind/nativewind) - Tailwind CSS for React Native.

## Testing & tooling

- [Maestro](https://github.com/mobile-dev-inc/maestro) - Painless end-to-end automation for mobile and web.
- [Appium](https://github.com/appium/appium) - Cross-platform automation framework for all kinds of apps.
- [Detox](https://github.com/wix/Detox) - Gray box end-to-end testing for React Native apps.
- [fastlane](https://github.com/fastlane/fastlane) - Automate building and releasing iOS and Android apps.
- [scrcpy](https://github.com/Genymobile/scrcpy) - Display and control Android devices from your computer.

## Learn mobile

- [Awesome Flutter](https://github.com/Solido/awesome-flutter) - Curated list of Flutter code and packages.
- [Awesome React Native](https://github.com/jondot/awesome-react-native) - Awesome components, news, apps and resources for React Native.
- [Awesome Android](https://github.com/JStumpp/awesome-android) - Curated list of awesome Android packages and resources.
- [Android Interview Questions](https://github.com/amitshekhariitbhu/android-interview-questions) - Your cheat sheet for Android interviews.

<!-- kb-guide:start -->

## Native or cross-platform?

Most teams today start with a cross-platform framework and go native only where they need it:

- **Flutter** compiles to native code and draws its own UI, so apps look identical on Android and iOS. A strong choice for custom, brand-heavy interfaces.
- **React Native with Expo** is the fastest path for teams that already know React and JavaScript or TypeScript. Expo handles builds, updates and many device APIs for you.
- **Kotlin Multiplatform and Compose Multiplatform** share business logic (and optionally UI) while keeping full access to native platform code. Popular with Android teams moving into iOS.
- **Ionic and Capacitor** wrap a web app in a native shell. Good for internal tools and content apps when you already have a web front end.
- **Native (Kotlin or Swift)** is still the best option for apps that depend heavily on the camera, background work, widgets or the newest platform features.

Whatever you choose, plan early for push notifications, deep links, offline storage, analytics and app store review — they take more time than the first screens.

## Frequently asked questions

??? question "Which framework should I learn first for mobile apps?"
    If you already know JavaScript, start with React Native and Expo. If you are starting from zero or want a very polished custom UI, Flutter is easier to learn as a whole package. For an Android-only career, learn Kotlin and Jetpack Compose.

??? question "Can I build an iOS app without a Mac?"
    You can write and test the code on Windows or Linux with Flutter or Expo, and use cloud build services such as Expo EAS to produce the iOS build. To publish on the App Store you still need an Apple Developer account.

??? question "How do I test a mobile app on real devices?"
    Use the emulators included with Android Studio and Xcode for daily work, then test on at least one real low-end Android phone. Tools such as Maestro and Detox automate end-to-end tests on devices.

## Keep exploring

- [iOS development](ios.md) · [Swift](swift.md) · [Flutter resources](library/flutter.md) · [Android resources](library/android.md)
- [Mobile web development](library/mobile-web-development.md) · [Testing & QA](testing.md)

<!-- kb-guide:end -->
