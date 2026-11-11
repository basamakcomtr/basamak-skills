"""Public Basamak Skills packaging smoke checks."""
from pathlib import Path
import os
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
NAMES = {"web-audit", "technical-troubleshooter", "support-assistant", "code-reviewer", "software-planner"}
INSTALL = ROOT / "scripts" / "install.sh"


class Tests(unittest.TestCase):
    def test_skills(self):
        self.assertEqual({p.name for p in SKILLS.iterdir() if p.is_dir()}, NAMES)
        for name in NAMES:
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"))
            self.assertIn(f"name: {name}\n", text.split("---\n", 2)[1])
            self.assertIn("description: >-\n", text.split("---\n", 2)[1])

    def test_docs(self):
        self.assertEqual((ROOT / "VERSION").read_text().strip(), "1.0.0")
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text())
        for path in ("README.md", "README.tr.md", "docs/installation.md",
                     "docs/kurulum.md", "CHANGELOG.md", "workflows/feature-request-to-review.md"):
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertNotIn("basamak-ai-skills/.agents",
                         (ROOT / "workflows/feature-request-to-review.md").read_text())

    def test_bash_syntax(self):
        subprocess.run(["bash", "-n", str(INSTALL)], check=True)

    def test_user_install_twice(self):
        with tempfile.TemporaryDirectory() as home:
            env = os.environ.copy()
            env["HOME"] = home
            for _ in range(2):
                subprocess.run(["bash", str(INSTALL), "--user"], env=env,
                               capture_output=True, text=True, check=True)
            for name in NAMES:
                link = Path(home) / ".agents" / "skills" / name
                self.assertTrue(link.is_symlink())
                self.assertEqual(link.resolve(), (SKILLS / name).resolve())

    def test_project_install(self):
        with tempfile.TemporaryDirectory() as project:
            subprocess.run(["bash", str(INSTALL), "--project", project],
                           check=True, capture_output=True, text=True)
            for name in NAMES:
                self.assertTrue((Path(project) / ".agents" / "skills" / name).is_symlink())

    def test_conflict_does_not_partially_install(self):
        with tempfile.TemporaryDirectory() as home:
            target = Path(home) / ".agents" / "skills"
            target.mkdir(parents=True)
            (target / "software-planner").mkdir()
            env = os.environ.copy()
            env["HOME"] = home
            p = subprocess.run(["bash", str(INSTALL), "--user"], env=env,
                               capture_output=True, text=True)
            self.assertNotEqual(p.returncode, 0)
            for name in NAMES - {"software-planner"}:
                self.assertFalse((target / name).exists())


if __name__ == "__main__":
    unittest.main()
