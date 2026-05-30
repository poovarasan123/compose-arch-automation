# compose-arch-automation
🚀 Python-based Clean Architecture generator for Android Jetpack Compose projects. Automatically creates scalable MVVM + Clean Architecture folder structures, Kotlin boilerplate files, package naming, ViewModels, State/Event classes, repositories, use cases, and Compose screens to speed up Android app development.

# Android Clean Architecture Generator

A lightweight Python-based automation tool that generates a scalable **Clean Architecture + MVVM** structure for Android projects using **Jetpack Compose**.

This script helps Android developers save time by automatically creating:

* Feature-based folder structure
* Kotlin boilerplate files
* ViewModels
* State & Event classes
* Repository interfaces & implementations
* UseCases
* Compose screens
* Package naming structure

Perfect for developers who frequently create new modules/features and want to maintain a clean and consistent architecture.

---

# 🚀 Features

## ✅ Automatic Folder Generation

Creates a complete Clean Architecture structure:

```text
feature/
 ├── data/
 │   ├── model/
 │   └── repository/
 ├── domain/
 │   ├── entity/
 │   ├── repository/
 │   └── usecase/
 └── presentation/
     ├── screen/
     ├── state/
     └── viewmodel/
```

---

## ✅ Kotlin Boilerplate Generation

Automatically generates:

* Data Models
* Entities
* Repository Interfaces
* Repository Implementations
* UseCases
* Jetpack Compose Screens
* ViewModels
* State Classes
* Event Classes

---

## ✅ Clean Package Naming

Automatically converts folders into proper Kotlin package names.

Example:

```kotlin
package com.<unit>.<app_name>.feature.<screen>.presentation.viewmodel
```

---

## ✅ Hilt Ready ViewModel

Generated ViewModels already include:

* `@HiltViewModel`
* `MutableStateFlow`
* `StateFlow`
* `viewModelScope`
* Event handling structure
* Base state management

---

## ✅ Compose Ready

Generated screen files already contain:

```kotlin
@Composable
fun SampleScreen() {
}
```

---

# 📂 Generated Structure Example

If you enter:

```text
Forgot Password
```

The script generates:

```text
feature/
 ├── data/
 │   ├── model/
 │   │   └── ForgotPasswordModel.kt
 │   └── repository/
 │       └── ForgotPasswordRepositoryImp.kt
 │
 ├── domain/
 │   ├── entity/
 │   │   └── ForgotPasswordEntity.kt
 │   ├── repository/
 │   │   └── ForgotPasswordRepository.kt
 │   └── usecase/
 │       └── ForgotPasswordUseCase.kt
 │
 └── presentation/
     ├── screen/
     │   └── ForgotPasswordScreen.kt
 │
     ├── state/
     │   ├── ForgotPasswordEvent.kt
     │   └── ForgotPasswordState.kt
 │
     └── viewmodel/
         └── ForgotPasswordViewModel.kt
```

---

# 🛠 Requirements

## Python

* Python 3.8+

Check version:

```bash
python --version
```

---

# 📥 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/android-clean-architecture-generator.git
```

```bash
cd android-clean-architecture-generator
```

---

# ▶️ Usage

## Option 1 — Using Batch File (Windows)

Run:

```bash
arch.bat
```

Then enter module name:

```text
Enter module name (e.g., Forgot Password): Login
```

---

## Option 2 — Direct Python Execution

```bash
python compose_arch.py
```

---

# ⚙️ Configuration

You can customize the base package inside:

```python
BASE_PACKAGE = "com.<unit>.<app_name>.feature"
```

Example:

```python
BASE_PACKAGE = "com.example.app.feature"
```

---

# 🧠 Generated Boilerplates

## ViewModel Includes

* StateFlow
* Event handling
* Hilt injection
* Coroutine scope
* Base UI state management

---

## State Class Includes

```kotlin
data class LoginState(
    val isLoading: Boolean = false,
    val onRefresh: Boolean = false,
    val error: String? = null,
    val message: String? = null,
    val sessionExpired: Boolean = false,
)
```

---

## Event Class Includes

```kotlin
sealed class LoginEvent {
    object OnRefresh : LoginEvent()
    object OnNavigationReset : LoginEvent()
    object ResetState : LoginEvent()
    object ResetErrorState : LoginEvent()
}
```

---

# 🔥 Benefits

✅ Faster feature/module creation
✅ Consistent architecture
✅ Reduces repetitive coding
✅ Better scalability
✅ Easier onboarding for teams
✅ Production-ready folder structure
✅ Helps maintain SOLID principles

---

# 📌 Best Use Cases

* Android projects with multiple modules/features
* Jetpack Compose apps
* MVVM architecture projects
* Clean Architecture projects
* Team-based Android development
* Rapid prototyping

---

# 🧩 Tech Stack

* Python
* Kotlin
* Jetpack Compose
* MVVM
* Clean Architecture
* Hilt
* Coroutines
* StateFlow

---

# 📈 Future Improvements

Planned features:

* Multi-module support
* XML layout support
* Retrofit API boilerplate generation
* Room database boilerplate
* Navigation graph generation
* DI module generation
* Unit test boilerplates
* KSP/KAPT support
* Gradle automation

---

# 🤝 Contributing

Contributions are welcome.

If you want to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 🐛 Issues

If you find any bugs or want improvements, create an issue in the repository.

---

# ⭐ Support

If this project helps you, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Poovarasan J

Android Developer | Mobile App Developer | Automation Enthusiast
