# Atlantia AI Design System - Guía Completa para Desarrolladores

## 📋 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Setup Inicial](#setup-inicial)
3. [Sistema de Colores](#sistema-de-colores)
4. [Tipografía](#tipografía)
5. [Componentes](#componentes)
6. [Patrones de Layout](#patrones-de-layout)
7. [Mejores Prácticas](#mejores-prácticas)
8. [Prompt para Cursor AI](#prompt-para-cursor-ai)

---

## 🎨 Introducción

Bienvenido al Design System de **Atlantia AI**, un sistema completo y profesional diseñado para crear interfaces modernas, consistentes y accesibles. Este UI Kit incluye más de 50 componentes organizados siguiendo las mejores prácticas de diseño.

### Características Principales

- ✅ **Paleta de colores oficial**: Violet, Purple, Lemon y Turquoise
- ✅ **Tipografía profesional**: Montserrat (300-800) y Hind
- ✅ **50+ Componentes**: Botones, inputs, tablas, cards, avatares y más
- ✅ **Modo oscuro**: Integrado en todos los componentes
- ✅ **Responsive**: Mobile-first design
- ✅ **Accesible**: WCAG 2.1 AA compliant
- ✅ **Optimizado para Cursor AI**: Prompts y código listo para copiar

---

## 🚀 Setup Inicial

### 1. Instalación de Dependencias

```bash
# Tailwind CSS v4
npm install tailwindcss@next @tailwindcss/typography

# Librerías de componentes
npm install lucide-react
npm install recharts
npm install sonner@2.0.3
npm install react-hook-form@7.55.0
npm install zod
npm install @iconify/react

# ShadCN UI (opcional, pero recomendado)
npx shadcn-ui@latest init
```

### 2. Configuración de Tailwind CSS v4

Crea o actualiza tu archivo `styles/globals.css`:

```css
@import "tailwindcss";

/* ========================================
   COLORES DE MARCA ATLANTIA AI
======================================== */
@theme {
  /* Colores Principales */
  --color-primary: #8345ba;  /* Color para inputs interactivos */
  --color-secondary: #aa49ca;
  --color-accent: #77c014;
  --color-turquoise: #04d1cd;
  --color-destructive: #d6215b;
  
  /* Colores de Estado */
  --color-success: #23b776;
  --color-warning: #f59e0b;
  --color-info: #3b82f6;
  
  /* Backgrounds */
  --color-background: #ffffff;
  --color-foreground: #021e3a;
  --color-card: #ffffff;
  --color-card-foreground: #021e3a;
  
  /* Tipografía */
  --font-sans: "Montserrat", system-ui, sans-serif;
  --font-display: "Hind", sans-serif;
}

/* Dark Mode */
@media (prefers-color-scheme: dark) {
  @theme {
    --color-background: #0a0a0a;
    --color-foreground: #ededed;
    --color-card: #1a1a1a;
    --color-card-foreground: #ededed;
  }
}

/* ========================================
   TIPOGRAFÍA BASE
======================================== */
body {
  font-family: var(--font-sans);
  font-weight: 400;
  color: var(--color-foreground);
  line-height: 1.55;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-sans);
  font-weight: 700;
  color: #482f91;
  line-height: 1.2;
}

h1 { 
  font-size: 48px; 
  font-weight: 800;
  line-height: 1.2;
}

h2 { 
  font-size: 36px; 
  font-weight: 700;
  line-height: 1.3;
}

h3 { 
  font-size: 24px; 
  font-weight: 600;
  line-height: 1.4;
}

h4 { 
  font-size: 20px; 
  font-weight: 600;
  line-height: 1.5;
}

p { 
  font-size: 16px; 
  line-height: 1.55;
}

/* ========================================
   UTILIDADES PERSONALIZADAS
======================================== */

/* Gradientes de texto */
.gradient-text-primary {
  background: linear-gradient(135deg, #482f91 0%, #aa49ca 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.gradient-text-accent {
  background: linear-gradient(135deg, #04d1cd 0%, #77c014 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Gradientes de fondo */
.gradient-bg-primary {
  background: linear-gradient(135deg, #482f91 0%, #aa49ca 100%);
}

.gradient-bg-accent {
  background: linear-gradient(135deg, #04d1cd 0%, #77c014 100%);
}

/* Animaciones */
@keyframes slide-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-slide-up {
  animation: slide-up 0.4s ease-out;
}

@keyframes slide-down {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-slide-down {
  animation: slide-down 0.3s ease-out;
}
```

### 3. Configuración de Fuentes (Next.js)

En tu archivo `app/layout.tsx`:

```tsx
import { Montserrat, Hind } from 'next/font/google';
import './globals.css';

const montserrat = Montserrat({ 
  subsets: ['latin'],
  weight: ['300', '400', '500', '600', '700', '800'],
  variable: '--font-sans'
});

const hind = Hind({ 
  subsets: ['latin'],
  weight: ['300', '400', '500', '600', '700'],
  variable: '--font-display'
});

export default function RootLayout({ 
  children 
}: { 
  children: React.ReactNode 
}) {
  return (
    <html lang="es" className={`${montserrat.variable} ${hind.variable}`}>
      <body>{children}</body>
    </html>
  );
}
```

---

## 🎨 Sistema de Colores

### Colores Principales

| Color | Uso |
|-------|-----|
| **Violet**<br>`#482F91`<br>`bg-[#482f91]`<br>`text-[#482f91]`<br>`border-[#482f91]` | Color primario, headings, elementos principales |
| **Purple**<br>`#AA49CA`<br>`bg-[#aa49ca]`<br>`text-[#aa49ca]`<br>`border-[#aa49ca]` | Color secundario, acentos, gradientes |
| **Lemon**<br>`#77C014`<br>`bg-[#77c014]`<br>`text-[#77c014]`<br>`border-[#77c014]` | Éxito, confirmación, elementos positivos |
| **Turquoise**<br>`#04D1CD`<br>`bg-[#04d1cd]`<br>`text-[#04d1cd]`<br>`border-[#04d1cd]` | Información, elementos interactivos |
| **Input Purple**<br>`#8345BA`<br>`bg-[#8345ba]`<br>`text-[#8345ba]`<br>`border-[#8345ba]` | **Color exclusivo para inputs interactivos** (Checkbox, Radio, Switch, Slider) |

### Colores de Estado

| Color | Uso |
|-------|-----|
| **Success**<br>`#23B776`<br>`bg-[#23b776]`<br>`text-[#23b776]`<br>`border-[#23b776]` | Éxito, confirmación |
| **Warning**<br>`#F59E0B`<br>`bg-[#f59e0b]`<br>`text-[#f59e0b]`<br>`border-[#f59e0b]` | Advertencias |
| **Destructive**<br>`#D6215B`<br>`bg-[#d6215b]`<br>`text-[#d6215b]`<br>`border-[#d6215b]` | Errores, acciones destructivas |
| **Info**<br>`#3B82F6`<br>`bg-[#3b82f6]`<br>`text-[#3b82f6]`<br>`border-[#3b82f6]` | Información |

### Uso en Código

```tsx
// Usando colores directos
<div className="bg-[#482f91] text-white">
  Contenido con color primario
</div>

// Usando gradientes de texto
<h1 className="gradient-text-primary">
  Título con Gradiente Atlantia
</h1>

// Gradiente diagonal en botón
<button className="bg-gradient-to-br from-[#482f91] to-[#aa49ca] text-white px-6 py-3 rounded-lg">
  Botón con Gradiente
</button>

// Hover states con colores
<button className="bg-[#aa49ca] hover:bg-[#8a3aaa] transition-colors">
  Hover Effect
</button>

// Bordes coloridos
<div className="border-2 border-[#aa49ca] rounded-lg p-6">
  Card con borde purple
</div>
```

---

## 📝 Tipografía

### Jerarquía Tipográfica

⚠️ **IMPORTANTE**: No uses clases de Tailwind para tamaño de fuente (`text-2xl`, `text-lg`, etc.), peso (`font-bold`), o line-height (`leading-none`) a menos que sea absolutamente necesario. El sistema global de tipografía en `globals.css` ya maneja estos estilos automáticamente.

```tsx
// ✅ CORRECTO - Usa los elementos HTML directamente
<h1>Título Principal</h1>       // 48px, weight: 800
<h2>Título Secundario</h2>      // 36px, weight: 700
<h3>Título Terciario</h3>       // 24px, weight: 600
<h4>Título Cuaternario</h4>     // 20px, weight: 600
<p>Texto de párrafo</p>         // 16px, weight: 400

// ✅ CORRECTO - Gradiente en headings
<h1 className="gradient-text-primary">
  Título con Gradiente
</h1>

// ✅ CORRECTO - Cambiar peso cuando sea necesario
<p className="font-semibold">Texto con más peso</p>

// ❌ INCORRECTO - No uses estas clases sin necesidad
<h2 className="text-3xl font-bold">Título</h2>
<p className="text-base leading-relaxed">Texto</p>
```

### Pesos de Fuente Disponibles

Montserrat incluye todos estos pesos:

```tsx
<p className="font-light">Light (300)</p>
<p className="font-normal">Regular (400)</p>
<p className="font-medium">Medium (500)</p>
<p className="font-semibold">Semibold (600)</p>
<p className="font-bold">Bold (700)</p>
<p className="font-extrabold">Extrabold (800)</p>
```

---

## 🧩 Componentes

Ver las secciones específicas en el UI Kit para ejemplos detallados de:

- **Botones**: Todas las variantes (primary, secondary, outline, ghost, destructive, link)
- **Inputs**: Input, Textarea, Select, Checkbox, Radio, Switch, Slider
- **Avatares**: InitialsAvatar personalizado con colores Atlantia
- **Tablas**: Tablas con toggle switches y acciones
- **Cards**: Cards con gradientes y efectos hover
- **Gráficas**: Recharts integrados con colores Atlantia
- **Iconos**: Iconify con +200,000 iconos disponibles

---

## 📐 Patrones de Layout

### Grids Responsive

```tsx
// Grid de 2 columnas
<div className="grid grid-cols-1 md:grid-cols-2 gap-6">
  <Card>Columna 1</Card>
  <Card>Columna 2</Card>
</div>

// Grid de 3 columnas
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <Card>Item 1</Card>
  <Card>Item 2</Card>
  <Card>Item 3</Card>
</div>

// Sidebar Layout
<div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
  <aside className="lg:col-span-1">
    <Card>Sidebar</Card>
  </aside>
  <main className="lg:col-span-3">
    <Card>Contenido Principal</Card>
  </main>
</div>
```

---

## ✅ Mejores Prácticas

### ✅ Hacer

1. **Usar los colores oficiales de Atlantia AI**
2. **Seguir la jerarquía tipográfica**
3. **Usar InitialsAvatar para avatares**
4. **Aplicar efectos hover consistentes**
5. **Usar rounded-[20px] para cards**
6. **Mantener espaciado consistente**
7. **Usar iconos de lucide-react o @iconify/react**
8. **Implementar responsive design**

### ❌ No Hacer

1. **No usar colores fuera de la paleta**
2. **No aplicar text-2xl, font-bold manualmente**
3. **No mezclar fuentes diferentes**
4. **No usar avatares de imágenes aleatorias**
5. **No ignorar estados hover**
6. **No usar border-radius inconsistentes**
7. **No crear versiones custom de componentes ShadCN**
8. **No usar estilos inline sin necesidad**

---

## 🤖 Prompt para Cursor AI

```
Estoy trabajando con el Design System de Atlantia AI. Por favor, sigue estas directrices:

**Colores de marca:**
- Primary: #482f91 (Violet)
- Secondary: #aa49ca (Purple)
- Accent: #77c014 (Lemon)
- Turquoise: #04d1cd
- Destructive: #d6215b
- Input Interactive: #8345ba

**Tipografía:**
- Font principal: Montserrat (pesos: 300-800)
- Font secundaria: Hind
- NO usar clases text-*, font-*, leading-* a menos que sea necesario
- Los H1-H4 y párrafos ya tienen estilos globales en globals.css

**Componentes:**
- Usar componentes de ShadCN UI desde ./components/ui/
- Usar InitialsAvatar para avatares de usuarios
- Usar MonthRangeCalendar para selectores de rango de meses
- Usar iconos de lucide-react o @iconify/react
- Aplicar efectos hover con elevación y sombras coloridas
- Color #8345BA para inputs interactivos (checkbox, radio, switch, slider)

**Layout:**
- Rounded corners: rounded-[20px] para cards, rounded-[8px] para botones
- Espaciado: múltiplos de 4 (p-4, p-6, gap-4, gap-6)
- Responsive: grid-cols-1 md:grid-cols-2 lg:grid-cols-3

**Colores de estado:**
- Success: #23b776
- Warning: #f59e0b
- Error: #d6215b

Genera el código siguiendo exactamente estas especificaciones y mantén el estilo profesional y moderno de Atlantia AI.
```

---

**© 2024 Atlantia AI - AI Innovations Test & Evaluation**
**Todos los derechos reservados.**