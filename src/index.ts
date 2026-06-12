export function greet(name: string): string {
  return `Hola, ${name}! Bienvenido a Curso.`;
}

if (require.main === module) {
  console.log(greet('mundo'));
}
