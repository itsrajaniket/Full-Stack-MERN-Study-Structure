const fs = require('fs');
const path = require('path');

const baseDir = path.resolve('..', 'MERN_Study_Structure');

const linkMap = [
    { pattern: /MDN Web Docs - HTML/i, link: 'https://developer.mozilla.org/en-US/docs/Web/HTML' },
    { pattern: /W3Schools - HTML/i, link: 'https://www.w3schools.com/html/' },
    { pattern: /MDN Web Docs - CSS/i, link: 'https://developer.mozilla.org/en-US/docs/Web/CSS' },
    { pattern: /W3Schools - CSS/i, link: 'https://www.w3schools.com/css/' },
    { pattern: /Bootstrap Official Docs/i, link: 'https://getbootstrap.com/docs/' },
    { pattern: /W3Schools Bootstrap/i, link: 'https://www.w3schools.com/bootstrap4/' },
    { pattern: /Tailwind CSS/i, link: 'https://tailwindcss.com/docs' },
    { pattern: /React Docs/i, link: 'https://react.dev/reference/react' },
    { pattern: /React Tutorial/i, link: 'https://react.dev/learn' },
    { pattern: /Next.js Official Docs/i, link: 'https://nextjs.org/docs' },
    { pattern: /Next.js Tutorial/i, link: 'https://nextjs.org/learn' },
    { pattern: /ShadCN Docs/i, link: 'https://ui.shadcn.com/docs' },
    { pattern: /Node.js/i, link: 'https://nodejs.org/docs/latest/api/' },
    { pattern: /Express.js/i, link: 'https://expressjs.com/' },
    { pattern: /NestJS Docs/i, link: 'https://docs.nestjs.com/' },
    { pattern: /JWT Authentication/i, link: 'https://jwt.io/introduction/' },
    { pattern: /MongoDB/i, link: 'https://www.mongodb.com/docs/manual/' },
    { pattern: /PostgreSQL/i, link: 'https://www.postgresql.org/docs/' },
    { pattern: /Prisma ORM/i, link: 'https://www.prisma.io/docs' },
    { pattern: /Mongoose/i, link: 'https://mongoosejs.com/docs/' },
    { pattern: /GitHub Docs/i, link: 'https://docs.github.com/' }
];

function walk(dir) {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const filePath = path.join(dir, file);
        if (fs.statSync(filePath).isDirectory()) {
            walk(filePath);
        } else if (file.endsWith('.md')) {
            let content = fs.readFileSync(filePath, 'utf8');
            let changed = false;

            linkMap.forEach(item => {
                // Only replace if it's not already a link
                // Looking for "- [ ] Name" patterns
                const regex = new RegExp(`- \\[([\\sx])\\] (${item.pattern.source})`, 'gi');
                if (regex.test(content)) {
                    content = content.replace(regex, (match, status, name) => {
                        // Check if the name itself isn't already inside a markdown link [name](link)
                        // This is a simple check, but enough for our structure
                        return `- [${status}] [${name}](${item.link})`;
                    });
                    changed = true;
                }
            });

            if (changed) {
                fs.writeFileSync(filePath, content);
                console.log(`  [LINKED] ${path.relative(baseDir, filePath)}`);
            }
        }
    });
}

console.log('Auto-linking resources in topic files...');
walk(baseDir);
console.log('Done!');
