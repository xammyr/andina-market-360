import os
import base64
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Diogo\Downloads\Proyecto_Completo_Andina_Market_360_GitHub\andina-market-360")
CAPTURAS_DIR = BASE_DIR / "evidencias" / "capturas"
HTML_OUT = BASE_DIR / "diapositivas.html"

INTEGRANTES = [
    "Guerrero Garcia Diogo Xammyr",
    "Simon Condori Sebastian Simon",
    "Huayta Cardenas RONALDHIÑO CRISTHIAN",
    "Casma Callañaupa Nick Arnold",
    "Neyra Ramos Jose Jeanpiere"
]

SLIDES_DATA = [
    {
        "id": "CAP01_E05",
        "img": "CAP01_E05.png",
        "cap": "Capítulo 01 · Introducción a GitHub",
        "titulo": "Línea de Base: Pruebas Unitarias y Cálculo de Ventas",
        "problema": "Verificar la exactitud matemática del negocio antes de cualquier control de versiones.",
        "comando": "python -m unittest discover -s tests -v && python src/resumen.py",
        "resultado": "4 pruebas unitarias aprobadas al 100%. Total consolidado de S/ 1,845.00 en 12 transacciones.",
        "guion": "Iniciamos el proyecto validando la lógica comercial: el script calcula automáticamente S/ 814 en Lima, S/ 555 en Ica y S/ 476 en Arequipa sin librerías externas."
    },
    {
        "id": "CAP02_E01",
        "img": "CAP02_E01.png",
        "cap": "Capítulo 02 · Configuración de Cuenta",
        "titulo": "Identidad Profesional y Parámetros de Seguridad",
        "problema": "Establecer la identidad técnica para auditar la autoría de cada cambio en el equipo.",
        "comando": "Configuración en github.com/xammyr + perfil_publico.md",
        "resultado": "Cuenta de GitHub configurada con higiene de credenciales, autenticación 2FA y perfil técnico.",
        "guion": "Configuramos la cuenta en GitHub con biografía profesional orientada a datos y políticas de seguridad sin exponer datos personales."
    },
    {
        "id": "CAP04_E01",
        "img": "CAP04_E01.png",
        "cap": "Capítulo 04 · Administración de Repositorios",
        "titulo": "Creación del Repositorio Remoto en GitHub",
        "problema": "Alojar el proyecto central para la colaboración y despliegue del equipo.",
        "comando": "GitHub UI: New Repository 'andina-market-360'",
        "resultado": "Repositorio creado vacío en la nube, listo para sincronizarse con el repositorio local.",
        "guion": "Creamos el repositorio remoto andina-market-360 sin archivos iniciales para permitir un push limpio desde nuestra estación de trabajo local."
    },
    {
        "id": "CAP06_E04",
        "img": "CAP06_E04.png",
        "cap": "Capítulo 06 · Instalación y Configuración de Git",
        "titulo": "Inicialización de Git Local y Primer Commit",
        "problema": "Iniciar el rastreo de versiones local y fijar la rama principal main.",
        "comando": "git init -b main && git add . && git commit -m 'chore: iniciar caso Andina Market'",
        "resultado": "Repositorio inicializado con rama main, .gitignore configurado y commit base registrado.",
        "guion": "Inicializamos Git en la máquina local usando la convención moderna de rama main y realizamos el commit inicial con todos los componentes base."
    },
    {
        "id": "CAP07_E01",
        "img": "CAP07_E01.png",
        "cap": "Capítulo 07 · Comandos Fundamentales",
        "titulo": "Detección Precisa de Modificaciones",
        "problema": "Revisar exactamente qué líneas cambiaron antes de preparar un commit.",
        "comando": "git status --short && git diff README.md",
        "resultado": "Identificación de cambios en el área de trabajo (Working Directory) con visualización de diferencias.",
        "guion": "Utilizamos git status y git diff para inspeccionar línea por línea las modificaciones antes de enviarlas al área de preparación."
    },
    {
        "id": "CAP07_E03",
        "img": "CAP07_E03.png",
        "cap": "Capítulo 07 · Comandos Fundamentales",
        "titulo": "Confirmación Atómica y Registro en Historial",
        "problema": "Registrar cambios documentales con mensajes estandarizados bajo Conventional Commits.",
        "comando": "git add README.md && git commit -m 'docs: actualizar notas de uso' && git log -1",
        "resultado": "Commit atómico creado con hash único y mensaje explicativo verificable en el historial.",
        "guion": "Confirmamos el cambio usando un mensaje con prefijo semántico 'docs:', garantizando trazabilidad para cualquier auditor del proyecto."
    },
    {
        "id": "CAP08_E01",
        "img": "CAP08_E01.png",
        "cap": "Capítulo 08 · Trabajo con Ramas",
        "titulo": "Aislamiento de Nuevas Funcionalidades",
        "problema": "Desarrollar mejoras visuales sin alterar la estabilidad de la rama principal main.",
        "comando": "git switch -c feature/resumen-sedes && git branch --show-current",
        "resultado": "Rama secundaria creada y activada; el entorno de desarrollo queda aislado.",
        "guion": "Aplicamos la regla de oro: nunca trabajar directo sobre main. Creamos la rama feature/resumen-sedes para desarrollar la mejora de cabeceras."
    },
    {
        "id": "CAP08_E02",
        "img": "CAP08_E02.png",
        "cap": "Capítulo 08 · Trabajo con Ramas",
        "titulo": "Desarrollo Aislado en la Rama Feature",
        "problema": "Incorporar el nuevo encabezado regional en la página web dentro de la rama.",
        "comando": "git add docs/index.html && git commit -m 'feat: agregar encabezado de sedes'",
        "resultado": "Commit registrado exclusivamente en la rama feature/resumen-sedes; main permanece intacta.",
        "guion": "Editamos el panel HTML incorporando el subtítulo regional y confirmamos el cambio únicamente dentro de la rama secundaria."
    },
    {
        "id": "CAP08_E05",
        "img": "CAP08_E05.png",
        "cap": "Capítulo 08 · Trabajo con Ramas",
        "titulo": "Fusión en Main y Limpieza de Ramas",
        "problema": "Integrar la funcionalidad probada a main y eliminar ramas que ya cumplieron su ciclo.",
        "comando": "git switch main && git merge feature/resumen-sedes && git branch -d feature/resumen-sedes",
        "resultado": "Historial unificado y rama secundaria eliminada de forma segura.",
        "guion": "Fusionamos la rama en main mediante merge y eliminamos la rama local ya integrada para mantener el repositorio limpio y ordenado."
    },
    {
        "id": "CAP09_E03",
        "img": "CAP09_E03.png",
        "cap": "Capítulo 09 · Sincronización Remota",
        "titulo": "Publicación de la Rama Principal hacia GitHub",
        "problema": "Subir los commits locales y establecer el tracking con el repositorio origin.",
        "comando": "git remote add origin https://github.com/... && git push -u origin main",
        "resultado": "Rama main vinculada a origin/main con transferencia completa de objetos.",
        "guion": "Vinculamos el repositorio remoto y ejecutamos el primer push con el flag -u para configurar el rastreo upstream automático."
    },
    {
        "id": "CAP09_E04",
        "img": "CAP09_E04.png",
        "cap": "Capítulo 09 · Sincronización Remota",
        "titulo": "Validación de Archivos en la Plataforma GitHub",
        "problema": "Verificar en la web que los árboles de directorios y commits coincidan con local.",
        "comando": "Navegación web en github.com/xammyr/andina-market-360",
        "resultado": "Todas las carpetas (data, src, tests, docs, evidencias) visibles en la nube.",
        "guion": "Comprobamos que todo el código fuente, la documentación y los datos sintéticos están correctamente respaldados en GitHub."
    },
    {
        "id": "CAP10_E01",
        "img": "CAP10_E01.png",
        "cap": "Capítulo 10 · Conflictos e Historial",
        "titulo": "Provocación Controlada de Conflicto en 3 Vías",
        "problema": "Simular dos desarrolladores modificando la misma línea en ramas paralelas.",
        "comando": "git merge prueba/alternativa-a (estando en prueba/alternativa-b)",
        "resultado": "Git detiene la fusión automática señalando CONFLICT (content) in notas_dashboard.md.",
        "guion": "Provocamos un conflicto controlado al editar la misma línea en dos ramas distintas para aprender el mecanismo interno de colisión de Git."
    },
    {
        "id": "CAP10_E02",
        "img": "CAP10_E02.png",
        "cap": "Capítulo 10 · Conflictos e Historial",
        "titulo": "Resolución Manual y Eliminación de Marcadores",
        "problema": "Integrar ambas propuestas técnicas eliminando los marcadores <<<<<<<, =======, >>>>>>>.",
        "comando": "Edición limpia de notas_dashboard.md && git add . && git commit -m 'fix: resolver conflicto'",
        "resultado": "Fusión completada exitosamente sin residuos de marcadores de conflicto.",
        "guion": "Resolvimos el conflicto unificando ambos enfoques, borramos los marcadores manuales y cerramos la fusión con un commit de fix trazable."
    },
    {
        "id": "CAP10_E03",
        "img": "CAP10_E03.png",
        "cap": "Capítulo 10 · Conflictos e Historial",
        "titulo": "Reversión Segura de Commits con git revert",
        "problema": "Deshacer un cambio erróneo sin reescribir ni destruir el historial compartido.",
        "comando": "git revert HEAD --no-edit && git log -2 --oneline",
        "resultado": "Nuevo commit de reversión creado; la historia se preserva completamente auditable.",
        "guion": "Utilizamos git revert en lugar de reset destructivo: Git crea un commit inverso que documenta cuándo y por qué se dio marcha atrás."
    },
    {
        "id": "CAP10_E04",
        "img": "CAP10_E04.png",
        "cap": "Capítulo 10 · Conflictos e Historial",
        "titulo": "Almacenamiento Temporal con git stash",
        "problema": "Guardar trabajo a medio hacer para cambiar de rama urgentemente sin hacer commit sucio.",
        "comando": "git stash push -m 'borrador' && git stash list && git stash pop",
        "resultado": "Área de trabajo limpia temporalmente y cambios restaurados posteriormente sin pérdidas.",
        "guion": "Guardamos cambios no confirmados con git stash, inspeccionamos la pila y recuperamos el trabajo con git stash pop sin perder ninguna edición."
    },
    {
        "id": "CAP10_E05",
        "img": "CAP10_E05.png",
        "cap": "Capítulo 10 · Conflictos e Historial",
        "titulo": "Auditoría Forense con git reflog",
        "problema": "Recuperar referencias a commits o ramas que ya no figuran en git log normal.",
        "comando": "git reflog -5",
        "resultado": "Historial cronológico completo de todos los movimientos de HEAD en la máquina.",
        "guion": "El reflog es la red de seguridad definitiva de Git: nos permite auditar cada salto de rama, checkout o commit incluso si fue eliminado."
    },
    {
        "id": "CAP11_E04",
        "img": "CAP11_E04.png",
        "cap": "Capítulo 11 · Herramientas Gráficas",
        "titulo": "Inspección Visual de Diferencias en VS Code",
        "problema": "Examinar cambios complejos mediante la interfaz Source Control de Visual Studio Code.",
        "comando": "VS Code Source Control (Ctrl+Shift+G) -> Vista Dividida (Side-by-side Diff)",
        "resultado": "Visualización clara de adiciones en verde y eliminaciones en rojo antes del commit.",
        "guion": "Demostramos el flujo gráfico en VS Code, comparando cambios lado a lado para verificar la exactitud antes de enviar a staging."
    },
    {
        "id": "CAP12_E04",
        "img": "CAP12_E04.png",
        "cap": "Capítulo 12 · Documentación con Markdown",
        "titulo": "Manual Operativo con Rutas Relativas y Bloques",
        "problema": "Crear documentación técnica portable que no se rompa al clonar en otros equipos.",
        "comando": "Renderizado de docs/manual.md y CONTRIBUTING.md",
        "resultado": "Manual con bloques de comando bash reproducibles y enlaces relativos hacia data/ventas.csv.",
        "guion": "Documentamos el proyecto con Markdown profesional usando rutas relativas para que los enlaces sigan funcionando en cualquier sistema operativo."
    },
    {
        "id": "CAP13_E01",
        "img": "CAP13_E01.png",
        "cap": "Capítulo 13 · GitHub Issues y Projects",
        "titulo": "Gestión de Requerimientos: Issue de Funcionalidad",
        "problema": "Registrar una nueva necesidad comercial con criterios de aceptación verificables.",
        "comando": "GitHub Issues: #1 feat: gráfico de ventas por sede en dashboard",
        "resultado": "Issue creado formalmente con checklist de requisitos cuantificables.",
        "guion": "Creamos el Issue #1 para planificar el gráfico regional con criterios de aceptación claros: lectura de JSON, participación y cero datos inventados."
    },
    {
        "id": "CAP13_E02",
        "img": "CAP13_E02.png",
        "cap": "Capítulo 13 · GitHub Issues y Projects",
        "titulo": "Gestión de Errores: Issue de Bug Reproducible",
        "problema": "Reportar técnicamente una falla con pasos exactos para reproducirla.",
        "comando": "GitHub Issues: #2 bug: discrepancia en total si se agregan filas sin recalcular",
        "resultado": "Reporte de bug estructurado con entrada, comportamiento observado y comportamiento esperado.",
        "guion": "Registramos el Issue #2 documentando el riesgo de desincronización entre el CSV y la web si no se ejecuta el script de actualización."
    },
    {
        "id": "CAP13_E04",
        "img": "CAP13_E04.png",
        "cap": "Capítulo 13 · GitHub Issues y Projects",
        "titulo": "Tablero Kanban Ágil en GitHub Projects",
        "problema": "Organizar visualmente el flujo de trabajo del equipo por estados de avance.",
        "comando": "GitHub Projects: Tablero Andina Market 360 (Columnas Ready, In progress, In review, Done)",
        "resultado": "Tarjetas de Issues vinculadas y movidas dinámicamente según el avance real.",
        "guion": "Implementamos un tablero Kanban en GitHub Projects para limitar el trabajo en progreso y gestionar de manera ágil los entregables del equipo."
    },
    {
        "id": "CAP14_E02",
        "img": "CAP14_E02.png",
        "cap": "Capítulo 14 · Pull Requests y Colaboración",
        "titulo": "Apertura Formal de Pull Request con Checklist",
        "problema": "Proponer cambios al equipo exigiendo verificación previa antes de tocar main.",
        "comando": "GitHub PR: feature/ficha-sedes -> main con plantilla de comprobación",
        "resultado": "Pull Request abierto con comparación de diff y checklist de pruebas unitarias cumplidas.",
        "guion": "Abrimos un Pull Request para la rama feature/ficha-sedes adjuntando la lista de verificación: pruebas locales pasadas y cero credenciales expuestas."
    },
    {
        "id": "CAP14_E05",
        "img": "CAP14_E05.png",
        "cap": "Capítulo 14 · Pull Requests y Colaboración",
        "titulo": "Fusión Formal de Pull Request (Merged)",
        "problema": "Integrar el código validado a main dejando evidencia histórica en GitHub.",
        "comando": "Botón 'Merge pull request' -> Confirm merge",
        "resultado": "Pull Request cerrado con estado 'Merged' (etiqueta morada) e historial unificado.",
        "guion": "Atendimos las observaciones del revisor y completamos el merge formal en GitHub, demostrando el ciclo colaborativo profesional completo."
    },
    {
        "id": "CAP18_E02",
        "img": "CAP18_E02.png",
        "cap": "Capítulo 18 · Versiones y Lanzamientos",
        "titulo": "Creación de Tag Anotado SemVer v1.0.0",
        "problema": "Etiquetar criptográficamente el punto exacto de la primera versión entregable.",
        "comando": "git tag -a v1.0.0 -m 'Primera version estable' && git show v1.0.0 --stat",
        "resultado": "Etiqueta inmutable apuntando al commit aprobado con autor, fecha y mensaje.",
        "guion": "Creamos el tag anotado v1.0.0 siguiendo el estándar de versionado semántico para marcar el primer hito estable del software comercial."
    },
    {
        "id": "CAP18_E04",
        "img": "CAP18_E04.png",
        "cap": "Capítulo 18 · Versiones y Lanzamientos",
        "titulo": "Publicación de la Release v1.0.0 en GitHub",
        "problema": "Poner a disposición de los usuarios los paquetes descargables y notas de cambios.",
        "comando": "git push origin v1.0.0 + GitHub Releases: Publish Release v1.0.0",
        "resultado": "Release pública con notas del CHANGELOG y código fuente empaquetado en ZIP/Tar.",
        "guion": "Publicamos la Release v1.0.0 en GitHub con las notas oficiales del CHANGELOG, permitiendo descargas reproducibles y seguras."
    },
    {
        "id": "CAP19_E04",
        "img": "CAP19_E04.png",
        "cap": "Capítulo 19 · GitHub Pages",
        "titulo": "Configuración del Despliegue en GitHub Pages",
        "problema": "Configurar la publicación web automática desde la carpeta /docs de main.",
        "comando": "Settings -> Pages -> Source: Deploy from a branch -> main /docs",
        "resultado": "Despliegue estático activado vinculado al pipeline nativo de GitHub Pages.",
        "guion": "Activamos GitHub Pages apuntando a la carpeta /docs de main, garantizando que el tablero web se actualice con cada commit aprobado."
    },
    {
        "id": "CAP19_E01",
        "img": "CAP19_E01.png",
        "cap": "Capítulo 19 · GitHub Pages",
        "titulo": "Dashboard Comercial en Vivo en Internet",
        "problema": "Exponer los resultados consolidados de ventas a gerencia en una URL pública.",
        "comando": "Acceso a https://xammyr.github.io/andina-market-360/",
        "resultado": "Sitio web responsivo y accesible mostrando los indicadores de Lima, Ica y Arequipa.",
        "guion": "Este es el resultado final visible para los usuarios: un tablero web alojado en la nube que lee los datos generados por Python sin costo de servidor."
    },
    {
        "id": "CAP21_E04",
        "img": "CAP21_E04.png",
        "cap": "Capítulos 21 y 22 · GitHub Actions (CI)",
        "titulo": "Integración Continua con Pruebas Automatizadas",
        "problema": "Prevenir que código con errores se fusione a main mediante validaciones automáticas.",
        "comando": "Pipeline .github/workflows/ci.yml ejecutando unittest discover",
        "resultado": "Workflow ejecutado en runner Ubuntu con check verde y 'Ran 4 tests ... OK'.",
        "guion": "Configuramos GitHub Actions para ejecutar las pruebas unitarias ante cada push: si un cálculo falla, la alerta roja bloquea la integración."
    },
    {
        "id": "CAP24_E03",
        "img": "CAP24_E03.png",
        "cap": "Capítulo 24 · Automatización Avanzada",
        "titulo": "Ejecución Matricial Multi-versión (Python 3.10 y 3.11)",
        "problema": "Garantizar compatibilidad del código en múltiples versiones del entorno de ejecución.",
        "comando": "strategy.matrix: python-version: ['3.10', '3.11']",
        "resultado": "Dos trabajos simultáneos ejecutados en paralelo y aprobados con éxito.",
        "guion": "Usamos matrices en CI para probar nuestro script tanto en Python 3.10 como en 3.11 en paralelo, asegurando compatibilidad multiplataforma."
    },
    {
        "id": "CAP26_E02",
        "img": "CAP26_E02.png",
        "cap": "Capítulo 26 · Seguridad de Dependencias",
        "titulo": "Escaneo y Parches Automáticos con Dependabot",
        "problema": "Mantener las acciones de GitHub actualizadas contra vulnerabilidades conocidas.",
        "comando": ".github/dependabot.yml (ecosistema github-actions con revisión semanal)",
        "resultado": "Dependabot abrió Pull Requests automáticos proponiendo actualizar acciones desactualizadas.",
        "guion": "Configuramos Dependabot para auditar nuestras dependencias de Actions: el bot crea PRs automáticos cuando detecta parches de seguridad."
    },
    {
        "id": "CAP27_E04",
        "img": "CAP27_E04.png",
        "cap": "Capítulo 27 · Auditoría y Calidad",
        "titulo": "Respaldo Forense Offline con git bundle",
        "problema": "Crear un respaldo completo del repositorio que no dependa de conexión a internet ni de GitHub.",
        "comando": "git bundle create andina-market.bundle --all && git bundle verify andina-market.bundle",
        "resultado": "Archivo único autocontenido con todo el historial de commits y ramas verificado.",
        "guion": "Generamos un paquete forense andina-market.bundle: un único archivo que contiene todo el historial de Git para recuperación ante desastres sin internet."
    },
    {
        "id": "CAP30_E01",
        "img": "CAP30_E01.png",
        "cap": "Capítulo 30 · Entornos Reproducibles",
        "titulo": "Contenedor Devcontainer para GitHub Codespaces",
        "problema": "Permitir que cualquier nuevo colaborador empiece a trabajar en segundos sin configurar nada.",
        "comando": "Archivo de configuración .devcontainer/devcontainer.json",
        "resultado": "Entorno Docker estandarizado basado en mcr.microsoft.com/devcontainers/python:3.",
        "guion": "Preparamos el devcontainer para Codespaces: con un solo clic, cualquier desarrollador levanta el entorno idéntico en un contenedor en la nube."
    },
    {
        "id": "CAP33_E02",
        "img": "CAP33_E02.png",
        "cap": "Capítulo 33 · Git Avanzado",
        "titulo": "Incorporación Selectiva con git cherry-pick",
        "problema": "Traer un commit específico de una rama experimental a main sin fusionar la rama completa.",
        "comando": "git switch main && git cherry-pick <HASH_COMMIT>",
        "resultado": "Commit específico trasplantado a main con nuevo hash y contenido integrado.",
        "guion": "Demostramos git cherry-pick: tomamos exclusivamente el commit de apunte analítico de una rama temporal y lo aplicamos limpiamente en main."
    },
    {
        "id": "CAP35_E01",
        "img": "CAP35_E01.png",
        "cap": "Capítulo 35 · Portafolio Profesional",
        "titulo": "Ficha Ejecutiva de Proyecto y Arquitectura",
        "problema": "Presentar los resultados técnicos y de negocio de forma clara a evaluadores o reclutadores.",
        "comando": "Renderizado de portfolio.md en VS Code / GitHub",
        "resultado": "Documento con resumen ejecutivo, métricas por sede, diagrama de arquitectura y competencias.",
        "guion": "El portafolio resume el valor del proyecto: cómo se integran los datos, la arquitectura del pipeline y las competencias profesionales adquiridas."
    },
    {
        "id": "CAP36_E03",
        "img": "CAP36_E03.png",
        "cap": "Capítulo 36 · Proyecto Integrador Final",
        "titulo": "Verificación Integral de la Solución (Ruta Completa)",
        "problema": "Demostrar que el proyecto cumple con el 100% de la rúbrica y funciona de inicio a fin.",
        "comando": "python -m unittest discover -s tests -v && python src/resumen.py --json && git status",
        "resultado": "4 pruebas unitarias OK, total S/ 1,845.00 cuadrado, y árbol de trabajo de Git limpio.",
        "guion": "Cerramos el proyecto integrador ejecutando la ruta completa: suite de pruebas pasando, JSON regenerado y repositorio en estado limpio y sincronizado."
    }
]

def img_to_base64(path):
    if not path.exists():
        return ""
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/png;base64,{data}"

def generar_slides():
    html_parts = ["""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Diapositivas · Andina Market 360 (Defensa y Sustentación)</title>
<style>
  @page {
    size: 297mm 210mm; /* A4 Horizontal / 16:9 widescreen */
    margin: 8mm;
  }
  * {
    box-sizing: border-box;
  }
  body {
    margin: 0;
    padding: 0;
    background: #0f172a;
    color: #f8fafc;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 13pt;
  }
  
  /* Diapositivas individuales */
  .slide {
    width: 100%;
    min-height: 100vh;
    padding: 30px 45px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
    position: relative;
    background: #0f172a;
  }
  
  /* Cabecera de Slide */
  .slide-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #1e293b;
    padding-bottom: 12px;
    margin-bottom: 16px;
  }
  .slide-cap {
    font-size: 11pt;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #38bdf8;
    font-weight: 700;
  }
  .slide-counter {
    background: #1e293b;
    color: #94a3b8;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 10pt;
    font-weight: 600;
  }
  .slide-title {
    font-size: 20pt;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 16px 0;
  }
  
  /* Cuerpo de la Diapositiva (Grid 2 columnas) */
  .slide-body {
    display: grid;
    grid-template-columns: 1fr 1.35fr;
    gap: 25px;
    flex: 1;
    align-items: center;
  }
  
  /* Panel Explicativo (Izquierda) */
  .text-panel {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .info-card {
    background: #1e293b;
    border-left: 4px solid #38bdf8;
    padding: 10px 14px;
    border-radius: 0 8px 8px 0;
  }
  .info-card.success {
    border-left-color: #22c55e;
  }
  .info-card.command {
    border-left-color: #f59e0b;
    background: #182234;
  }
  .info-card.speech {
    border-left-color: #a855f7;
    background: #1e1b4b;
  }
  
  .card-label {
    font-size: 9.5pt;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.5px;
    color: #94a3b8;
    margin-bottom: 3px;
  }
  .card-label.cmd { color: #f59e0b; }
  .card-label.succ { color: #22c55e; }
  .card-label.spk { color: #c084fc; }
  
  .card-content {
    font-size: 10.5pt;
    color: #e2e8f0;
    line-height: 1.4;
  }
  code.cmd-text {
    font-family: Consolas, monospace;
    font-size: 9.5pt;
    color: #fde047;
    word-break: break-all;
  }
  
  /* Panel de Imagen (Derecha) */
  .img-panel {
    background: #020617;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    max-height: 520px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.5);
  }
  .evidence-image {
    max-width: 100%;
    max-height: 500px;
    object-fit: contain;
    border-radius: 4px;
  }

  /* Pie de Slide */
  .slide-footer {
    display: flex;
    justify-content: space-between;
    font-size: 9pt;
    color: #64748b;
    border-top: 1px solid #1e293b;
    padding-top: 8px;
    margin-top: 14px;
  }
  
  /* Portada Especial */
  .slide-cover {
    justify-content: center;
    align-items: center;
    text-align: center;
    background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%);
  }
  .cover-badge {
    background: rgba(56, 189, 248, 0.15);
    color: #38bdf8;
    border: 1px solid #38bdf8;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 11pt;
    font-weight: 700;
    margin-bottom: 20px;
  }
  .cover-title {
    font-size: 34pt;
    font-weight: 900;
    color: #ffffff;
    margin: 0 0 10px 0;
    letter-spacing: -0.5px;
  }
  .cover-sub {
    font-size: 17pt;
    color: #94a3b8;
    margin: 0 0 35px 0;
  }
  .cover-team {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 20px 30px;
    max-width: 750px;
    width: 100%;
    margin-bottom: 25px;
    text-align: left;
  }
  .cover-team-title {
    font-size: 11pt;
    text-transform: uppercase;
    color: #38bdf8;
    font-weight: 700;
    margin-bottom: 12px;
    border-bottom: 1px solid #334155;
    padding-bottom: 6px;
  }
  .cover-team-list {
    margin: 0;
    padding-left: 24px;
    line-height: 1.7;
    font-size: 12pt;
    color: #f1f5f9;
  }
  .cover-links {
    display: flex;
    gap: 20px;
    font-size: 11pt;
    color: #94a3b8;
  }
  .cover-links a {
    color: #38bdf8;
    text-decoration: none;
    font-weight: 600;
  }

  /* Controles de Navegación en Pantalla */
  .nav-controls {
    position: fixed;
    bottom: 20px;
    right: 25px;
    display: flex;
    gap: 10px;
    z-index: 1000;
  }
  .nav-btn {
    background: #38bdf8;
    color: #0f172a;
    border: none;
    padding: 10px 18px;
    border-radius: 20px;
    font-weight: 700;
    cursor: pointer;
    font-size: 11pt;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
  }
  .nav-btn:hover {
    background: #7dd3fc;
  }

  @media print {
    .nav-controls { display: none !important; }
    .slide {
      min-height: 100vh;
      height: 100vh;
      page-break-after: always;
      page-break-inside: avoid;
    }
  }
</style>
</head>
<body>

<div class="nav-controls">
  <button class="nav-btn" onclick="prevSlide()">◀ Anterior</button>
  <button class="nav-btn" onclick="nextSlide()">Siguiente ▶</button>
</div>

<!-- SLIDE 1: PORTADA -->
<div class="slide slide-cover" id="slide-1">
  <div class="cover-badge">DEFENSA DEL PROYECTO INTEGRADOR · RÚBRICA 100/100</div>
  <h1 class="cover-title">Andina Market 360</h1>
  <div class="cover-sub">Sustentación de Prácticas: De una Hoja CSV a un Repositorio Publicado y Probado</div>
  
  <div class="cover-team">
    <div class="cover-team-title">Integrantes del Equipo de Exposición:</div>
    <ol class="cover-team-list">
"""]

    for persona in INTEGRANTES:
        html_parts.append(f"      <li><strong>{persona}</strong></li>\n")

    html_parts.append("""    </ol>
  </div>
  
  <div class="cover-links">
    <div>🐙 Repositorio: <a href="https://github.com/xammyr/andina-market-360">github.com/xammyr/andina-market-360</a></div>
    <div>🌐 Dashboard en Vivo: <a href="https://xammyr.github.io/andina-market-360/">xammyr.github.io/andina-market-360/</a></div>
  </div>
</div>
""")

    total_slides = len(SLIDES_DATA) + 1  # portada + evidencias

    for idx, s in enumerate(SLIDES_DATA, start=2):
        img_path = CAPTURAS_DIR / s["img"]
        b64 = img_to_base64(img_path)
        
        html_parts.append(f"""
<!-- SLIDE {idx}: {s['id']} -->
<div class="slide" id="slide-{idx}">
  <div class="slide-header">
    <div class="slide-cap">{s['cap']}</div>
    <div class="slide-counter">Diapositiva {idx} / {total_slides}</div>
  </div>
  
  <h2 class="slide-title">{s['titulo']}</h2>
  
  <div class="slide-body">
    <div class="text-panel">
      <div class="info-card">
        <div class="card-label">🎯 Objetivo / Desafío</div>
        <div class="card-content">{s['problema']}</div>
      </div>
      
      <div class="info-card command">
        <div class="card-label cmd">💻 Comando / Acción Ejecutada</div>
        <div class="card-content"><code class="cmd-text">{s['comando']}</code></div>
      </div>
      
      <div class="info-card success">
        <div class="card-label succ">✅ Resultado Verificado</div>
        <div class="card-content">{s['resultado']}</div>
      </div>
      
      <div class="info-card speech">
        <div class="card-label spk">🎤 Guion para Exponer (Qué decir)</div>
        <div class="card-content"><em>"{s['guion']}"</em></div>
      </div>
    </div>
    
    <div class="img-panel">
      <img src="{b64}" class="evidence-image" alt="{s['titulo']}">
    </div>
  </div>
  
  <div class="slide-footer">
    <div>Caso Empresarial Andina Market 360 · Evidencia Oficial: <code>{s['id']}</code></div>
    <div>Universidad / Trabajo S15 · Git y GitHub Profesional</div>
  </div>
</div>
""")

    # Script interactivo para navegación con teclado
    html_parts.append("""
<script>
  let currentSlide = 1;
  const total = document.querySelectorAll('.slide').length;

  function goToSlide(n) {
    if (n < 1) n = 1;
    if (n > total) n = total;
    currentSlide = n;
    const target = document.getElementById('slide-' + currentSlide);
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  }

  function nextSlide() {
    goToSlide(currentSlide + 1);
  }

  function prevSlide() {
    goToSlide(currentSlide - 1);
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'Space') {
      nextSlide();
    } else if (e.key === 'ArrowLeft') {
      prevSlide();
    }
  });
</script>
</body>
</html>
""")

    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write("".join(html_parts))
    print(f"Diapositivas HTML generadas exitosamente en {HTML_OUT}")

if __name__ == "__main__":
    generar_slides()
