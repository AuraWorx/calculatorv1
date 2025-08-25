# Calculator API - CI/CD Learning Project

This project is designed to help you learn about **Pull Requests**, **GitHub Environments**, **Release-please**, and **Semantic Versioning** in a real CI/CD pipeline.

## 🎯 **What You'll Learn**

- **Pull Request Workflow**: Feature → Develop → Main
- **GitHub Environments**: Development, UAT, Production
- **Release-please**: Automated semantic versioning and releases
- **Semantic Versioning**: Conventional commits and version bumping
- **CI/CD Pipeline**: Automated testing and deployment

## 🚀 **Project Structure**

```
calculator-api/
├── app/                    # Simple FastAPI calculator
├── tests/                  # Test files
├── .github/
│   ├── workflows/          # CI/CD workflows
│   └── release-please.yml  # Release automation
├── .release-please-config.json  # Release configuration
└── CHANGELOG.md            # Auto-updated changelog
```

## 🔄 **Complete Workflow**

### **1. Feature Branch Development**
```bash
# Create feature branch from develop
git checkout develop
git pull origin develop
git checkout -b feature/calculator-enhancement

# Make changes and commit with conventional commit format
git add .
git commit -m "feat: add power operation to calculator"
git push origin feature/calculator-enhancement
```

**What happens:**
- Feature branch CI runs (non-blocking SonarCloud)
- Tests pass, code quality checks pass
- Ready for PR to develop

### **2. PR to Develop Branch**
```bash
# Create PR from feature to develop
# GitHub will show: "Compare & pull request"
```

**What happens:**
- Develop branch CI runs (blocking SonarCloud)
- All tests must pass
- Code quality gates must pass
- **Auto-deploy to Development Environment**
- PR can be merged to develop

### **3. PR to Main Branch**
```bash
# Create PR from develop to main
# This triggers the release process
```

**What happens:**
- Main branch CI runs (blocking + integration tests)
- All quality gates must pass
- **Release-please automatically creates a release PR**
- Release PR contains version bump and changelog updates

### **4. Release and Deployment**
```bash
# Merge the release PR to main
# This creates a new tag (e.g., v1.1.0)
```

**What happens:**
- **Auto-deploy to UAT Environment**
- **Manual approval required for Production**
- New version is created based on conventional commits

## 🏗️ **GitHub Environments**

### **Development Environment**
- **Trigger**: Merge to `develop` branch
- **Deployment**: Automatic
- **URL**: https://dev-calculator-api.example.com
- **Purpose**: Integration testing, feature validation

### **UAT Environment**
- **Trigger**: Release tag creation
- **Deployment**: Automatic
- **URL**: https://uat-calculator-api.example.com
- **Purpose**: User acceptance testing, staging

### **Production Environment**
- **Trigger**: UAT deployment success
- **Deployment**: Manual approval required
- **URL**: https://prod-calculator-api.example.com
- **Purpose**: Live production system

## 📝 **Conventional Commits**

Release-please uses conventional commits to determine version bumps:

```bash
# Patch version (1.0.0 → 1.0.1)
git commit -m "fix: resolve division by zero error"

# Minor version (1.0.0 → 1.1.0)
git commit -m "feat: add power operation"

# Major version (1.0.0 → 2.0.0)
git commit -m "feat!: breaking change in API response format"

# Other types (no version bump)
git commit -m "docs: update API documentation"
git commit -m "test: add integration tests"
git commit -m "chore: update dependencies"
```

## 🚀 **Release-please Workflow**

### **Automatic Release Creation**
1. **Main branch CI passes** → Release-please workflow triggers
2. **Release PR created** → Contains version bump and changelog
3. **Review and merge** → Creates new git tag
4. **Tag triggers deployment** → UAT → Production

### **Version Bumping Rules**
- `feat:` → Minor version bump (1.0.0 → 1.1.0)
- `fix:` → Patch version bump (1.0.0 → 1.0.1)
- `feat!:` → Major version bump (1.0.0 → 2.0.0)
- `docs:`, `test:`, `chore:` → No version bump

## 🧪 **Testing the Workflow**

### **Step 1: Setup Repository**
1. Push this code to a new GitHub repository
2. Create `develop` branch
3. Set up GitHub Environments (Development, UAT, Production)
4. Add required secrets (SONAR_TOKEN)

### **Step 2: Feature Development**
```bash
git checkout develop
git checkout -b feature/test-feature
# Make a small change
git commit -m "feat: add simple logging"
git push origin feature/test-feature
```

### **Step 3: Create PRs**
1. **Feature → Develop**: Tests run, auto-deploy to Dev
2. **Develop → Main**: Integration tests, release-please triggers

### **Step 4: Watch Release Process**
1. Release PR created automatically
2. Merge release PR
3. New tag created (e.g., v1.1.0)
4. UAT deployment starts
5. Production deployment waits for approval

## 📊 **CI/CD Pipeline Stages**

### **Feature Branch CI**
- ✅ Linting and formatting
- ✅ Unit tests (80% coverage)
- ✅ SonarCloud scan (non-blocking)

### **Develop Branch CI**
- ✅ Linting and formatting
- ✅ Unit tests (80% coverage)
- ✅ SonarCloud scan (blocking)
- 🚀 **Auto-deploy to Development**

### **Main Branch CI**
- ✅ Linting and formatting
- ✅ Unit tests (80% coverage)
- ✅ Integration tests
- ✅ SonarCloud scan (blocking)
- 🚀 **Trigger release-please**

### **Release Workflow**
- 🚀 **Auto-deploy to UAT**
- 🔒 **Manual approval for Production**
- 🚀 **Deploy to Production**

## 🎉 **What You'll See**

1. **Feature Branch**: CI runs, tests pass
2. **PR to Develop**: CI runs, auto-deploys to Dev
3. **PR to Main**: CI runs, release-please creates release PR
4. **Release PR**: Contains version bump and changelog
5. **Merge Release**: Creates tag, triggers UAT deployment
6. **UAT Success**: Production deployment waits for approval
7. **Production Approval**: Final deployment completes

## 🔧 **Configuration Files**

- **`.release-please-config.json`**: Release automation settings
- **`.github/release-please.yml`**: Release workflow
- **`.github/workflows/`**: CI/CD pipelines
- **`CHANGELOG.md`**: Auto-updated changelog

## 📚 **Learning Resources**

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Release-please Documentation](https://github.com/google-github-actions/release-please-action)
- [GitHub Environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)
- [Semantic Versioning](https://semver.org/)

## 🚀 **Ready to Learn!**

This project gives you a complete, working example of:
- **Pull Request workflows**
- **GitHub Environments**
- **Automated releases**
- **Semantic versioning**
- **CI/CD pipelines**

Start by creating a feature branch and watch the magic happen! 🎯
