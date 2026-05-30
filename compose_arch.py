import os

BASE_PACKAGE = "com.tt.rakchat.feature"  # root package

# Directory -> files -> file type
structure = {
    "data/model": [("Model", "class")],
    "data/repository": [("RepositoryImp", "class")],
    "domain/entity": [("Entity", "data_class")],
    "domain/usecase": [("UseCase", "data_class")],
    "domain/repository": [("Repository", "interface")],
    "presentation/screen": [("Screen", "composable")],
    "presentation/viewmodel": [("ViewModel", "class_viewmodel")],
    "presentation/state": [("Event", "sealed_class"), ("State", "data_class")],
}


def get_package(folder: str, module_name: str) -> str:
    """Convert folder path into proper Kotlin package name with module."""
    normalized = os.path.normpath(folder)            # convert to system path
    package_path = normalized.replace(os.sep, ".")   # replace / or \ with .
    return f"{BASE_PACKAGE}.{module_name.replace(" ", "_").lower()}.{package_path}"


def generate_kotlin_content(name: str, suffix: str, file_type: str, package_name: str) -> str:
    """Return Kotlin boilerplate based on type."""

    full_name = f"{name}{suffix}"

    if file_type == "class":
        return f"""package {package_name}

class {full_name} {{
}}
"""

    if file_type == "class_viewmodel":
        return f"""package {package_name}

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import javax.inject.Inject
import {package_name.replace("presentation", "presentation.state").replace("viewmodel","")}{full_name.replace("ViewModel","")}Event
import {package_name.replace("presentation", "presentation.state").replace("viewmodel","")}{full_name.replace("ViewModel","")}State

@HiltViewModel
class {full_name} @Inject constructor(private val appPreferences: AppPreferences) : ViewModel() {{

    private val _state = MutableStateFlow({full_name.replace("ViewModel","")}State())
    val state: StateFlow<{full_name.replace("ViewModel","")}State> = _state.asStateFlow()

    fun onEvent(event: {full_name.replace("ViewModel","")}Event) {{
        when (event) {{
            is {full_name.replace("ViewModel","")}Event.OnRefresh -> {{
            }}
            is {full_name.replace("ViewModel","")}Event.OnNavigationReset -> {{
            }}
            is {full_name.replace("ViewModel","")}Event.ResetState -> {{
                _state.value = {full_name.replace("ViewModel","")}Event.ResetState()
            }}
            is {full_name.replace("ViewModel","")}State -> {{
                _state.value = _state.value.copy(error = null, message = null)
            }}
        }}
    }}

    fun doSomething() {{
        viewModelScope.launch {{
            // TODO: Implement logic
        }}
    }}
}}
"""

    if file_type == "interface":
        return f"""package {package_name}

interface {full_name} {{
    // TODO: Define repository methods
}}
"""

    if file_type == "data_class":
        return f"""package {package_name}

data class {full_name}(
    val isLoading: Boolean = false,
    val onRefresh: Boolean = false,
    val error: String? = null,
    val message: String? = null,
    val sessionExpired: Boolean = false,
)
"""

    if file_type == "sealed_class":
        return f"""package {package_name}

sealed class {full_name} {{
    object OnRefresh : {full_name}()
    object OnNavigationReset : {full_name}()
    object ResetState : {full_name}()
    object ResetErrorState : {full_name}()
}}
"""

    if file_type == "composable":
        return f"""package {package_name}

import androidx.compose.runtime.Composable

@Composable
fun {full_name}() {{
    // TODO: Implement UI
}}
"""

    return f"""package {package_name}

// TODO: Implement {full_name}
"""


def create_clean_architecture(module_name: str, base_path="."):
    pascal_name = "".join(word.capitalize() for word in module_name.split())

    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"📂 Created: {folder_path}")

        package_name = get_package(folder, module_name)

        for suffix, file_type in files:
            file_name = f"{pascal_name}{suffix}.kt"
            file_path = os.path.join(folder_path, file_name)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write(generate_kotlin_content(pascal_name, suffix, file_type, package_name))
                print(f"   📝 Created: {file_path}")
            else:
                print(f"   ⚠️ Skipped (already exists): {file_path}")


if __name__ == "__main__":
    module_name = input("Enter module name (e.g., Forgot Password): ")
    base_path = "."
    create_clean_architecture(module_name, base_path)
    print("\n✅ Clean Architecture setup completed with Kotlin boilerplates + package names!")
