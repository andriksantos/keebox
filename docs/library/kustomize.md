---
title: "Kustomize – Awesome List with 26 resources"
description: "26 curated Kustomize resources: Kubernetes native declarative configuration management tool."
---

# Kustomize

Kubernetes native declarative configuration management tool.

!!! info "Source"
    26 resources imported from [DevOpsHiveHQ/awesome-kustomize](https://github.com/DevOpsHiveHQ/awesome-kustomize), dedicated to the public domain ([CC0 / Unlicense](https://creativecommons.org/publicdomain/zero/1.0/)). Thanks to its maintainers and contributors. Part of the [KEEBOX Library](index.md) · Category: **Back-End Development**.

<!-- kb-about:start -->

## About this list

**Kustomize** — kubernetes native declarative configuration management tool. This page brings together 11 links about Kustomize, grouped into 3 sections. The largest sections are **Plugins**, **Snippets**, **Misc**, a good place to start if you are exploring the topic for the first time. It belongs to the **Back-End Development** category of the KEEBOX Library; see the related lists at the end of the page for neighbouring topics.

### What you'll find

- **Plugins** — 9 links
- **Snippets** — 1 link
- **Misc** — 1 link

<!-- kb-about:end -->

## Plugins

### Generators

- [Secretize](https://github.com/bbl/secretize) - Generating Kubernetes Secret from various sources. It's like a Swiss Army knife, but for Kubernetes secrets (Containerized KRM, Exec KRM, Exec).
- [SopsSecretGenerator](https://github.com/goabout/kustomize-sopssecretgenerator/) - Generating Secrets from sops-encrypted files (Exec KRM, Exec).
- [KSops](https://github.com/viaduct-ai/kustomize-sops) - Generating Secrets from sops-encrypted files (Exec).
- [PolicyGenerator](https://github.com/open-cluster-management-io/policy-generator-plugin) - Generating Open Cluster Management policies (Exec).
- [KRMFfnBuiltin](https://github.com/kaweezle/krmfnbuiltin) - Running builtin generators transformers (Exec).
- [Merger](https://github.com/aabouzaid/kustomize-plugin-merger) - Generating manifests seamlessly by extending Kustomize merge strategies using schemaless StrategicMerge (Containerized KRM, Exec KRM).

### Transformers

- [HelmValuesTransformer](https://github.com/openinfradev/kustomize-helm-transformer) - Transforming values in HelmRelease CustomResource. It helps manage many HelmRelease values in a single transformer file (Exec).
- [TemplateTransformer](https://github.com/joshdk/template-transformer) - Providing a set of KRM Functions to run built-in transformers in place (Containerized KRM, Exec KRM).

### Validators

- [KubeconformValidator](https://github.com/aabouzaid/kustomize-kubeconformvalidator) - Validating Kubernetes manifests using embedded Kubeconform (Containerized KRM, Exec KRM).

## Guides

### Novice

- 📰 [Declarative Management of Kubernetes Objects Using Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) - The official Kubernetes documentation task for Kustomize.
- 📰 [Configure Kubernetes with Kustomize](https://cloud.google.com/anthos-config-management/docs/concepts/kustomize) - A guide helps to get started with Kustomize, understand its intended use cases, and find resources for using it with other Google Cloud tools.
- 📺 [Organizing the YAML mess with Kustomize](https://www.youtube.com/watch?v=1fCAwFGX38U) - A talk shows how Kustomize could help to manage Kubernetes YAML files with a growing number of services and environments.
- 📺 [Kustomize: Deploy Your App with Template Free YAML](https://www.youtube.com/watch?v=ahMIBxufNR0) - A talk introduces Kustomize, a declarative application management system that allows deployments to be described as template-free YAML.

### Intermediate

- 🧪 [ArgoCD GitOps Tutorial - Working with Kustomize](https://redhat-scholars.github.io/argocd-tutorial/argocd-tutorial/03-kustomize.html) - A hands-on lab covers using Kustomize in GitOps, and it goes through the Kustomize syntax and deploying a Kustomized application.
- 📰 [3 ways to customize off-the-shelf Helm charts with Kustomize](https://tech.aabouzaid.com/2020/09/3-ways-to-customize-off-the-shelf-helm-charts-with-kustomize-kubernetes.html) - A guide covers 3 different ways to use Kustomize and Helm together.
- 📰 [Using Kustomize Components with Cluster API](https://blog.scottlowe.org/2021/11/01/using-kustomize-components-with-cluster-api/) - A clear use case of using Kustomize Components.

### Advanced

- 📰 [Advanced Kustomize features](https://www.innoq.com/en/blog/advanced-kustomize-features/) - A guide covers more than 5 advanced Kustomize capabilities.
- 📰 [Set OpenAPI patch strategy for Kubernetes Custom Resources](https://tech.aabouzaid.com/2022/11/set-openapi-patch-strategy-for-kubernetes-custom-resources-kustomize.html) - A guide shows how to provide a schema to control the patch strategy of the CRDs.
- 📺 [Customizing Kustomize with Client-Side Custom Resources](https://www.youtube.com/watch?v=YlFUv4F5PYc) - A talk covers extending Kustomize via plugins to address common yet idiosyncratic application needs.
- 📺 [Own your YAML: extending Kustomize via Plugins](https://www.youtube.com/watch?v=Xoh_OpLoVtI) - A talk shows how to create custom resources using Kustomize external plugins.
- 📰 [Kustomize Enhancement with KRM Functions](https://www.innoq.com/en/blog/kustomize-enhancement-with-krm-functions/) - A detailed guide covers the KRM concept and how to use it in Kustomize plugins.

### Tips & Tricks

- 📰 [Delete a manifest from a Kustomize base](https://tech.aabouzaid.com/2021/05/delete-a-manifest-from-kustomize-base.html) - A handy way to delete a named manifest using Kustomize patch.
- 📰 [Apply Kustomize builtin transformers on a single resource](https://tech.aabouzaid.com/2022/04/apply-kustomize-builtin-transformers-on-a-single-resource.html) - A way to use internal transformers on specific resources.
- 📰 [Pass extra data to the Containerized KRM function](https://tech.aabouzaid.com/2022/12/pass-extra-data-to-the-containerized-krm-function.html) - Different cases of sharing data with the Containerized KRM function.

## Snippets

- [Add Pod security context](https://github.com/3deep5me/awesome-kustomize/blob/add-security-context-component/snippets/add-pod-security-context/kustomization.yaml) - Ensure the security context is added to containers in the Pod.

## Misc

- [Asdf-kustomize](https://github.com/Banno/asdf-kustomize) - Kustomize plugin for asdf version manager.

<!-- kb-related:start -->

## Related lists

More lists in the **Back-End Development** category of the [KEEBOX Library](index.md):

- [Lumen](lumen.md)
- [nginx](nginx.md)
- [OpenTofu](opentofu.md)
- [Play1 Framework](play1-framework.md)
- [Education](education.md)
- [FastAPI](fastapi.md)
- [Flask](flask.md)
- [IAM](iam.md)

<!-- kb-related:end -->
